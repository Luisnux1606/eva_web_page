from django import template
from ..models import Page

register = template.Library()

@register.simple_tag   #register the function in library as a simple_tag
def get_page_list():
    pages = Page.objects.all()
    return pages

