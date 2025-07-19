from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import *
from utils.views import DataMixin

class HomePage(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['networks'] = SocialNetwork.objects.all().order_by('-order')
        context['news'] = News.objects.all().order_by('-created_at')[:6]
        context['main_slides'] = MainSlider.objects.all()
        context['podcast_channels'] = PodcastChannel.objects.prefetch_related('releases')
        context['podcast_release_list'] = PodcastRelease.objects.all().order_by('-created_at')[:6]

        return context

  
class NewsListView(DataMixin, ListView):
    template_name = 'blog/blog-list.html'
    model = News
    paginate_by = 12

class NewsDetailView(DetailView):
    template_name = 'blog/blog-detail.html'
    model = News

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        news = context['object']
        news.views += 1
        news.save()
        context['popular_news'] = News.objects.order_by('-views')[:3]
        context['resent_news'] = News.objects.order_by('-created_at')[:3]

        return context


class PodcastListView(DataMixin, ListView):
    template_name = 'podcast/podcast-list.html'
    model = PodcastRelease
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['channels'] = PodcastChannel.objects.prefetch_related('releases').all()
        return context

class AboutUs(TemplateView):
    template_name = 'about-us.html'