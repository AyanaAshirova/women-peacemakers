from django import template
from main.models import SocialNetwork

register = template.Library()

@register.simple_tag(takes_context=True)
def get_networks(context):
    return SocialNetwork.objects.all()
