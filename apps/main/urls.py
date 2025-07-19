from .views import *
from django.urls import path, include

urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('news/', NewsListView.as_view(), name='news'),
    path('news/<pk>', NewsDetailView.as_view(), name='news-details'),
    path('podcast/', PodcastListView.as_view(), name='podcast'),
    path('about-us/', AboutUs.as_view(), name='about-us'),
]
