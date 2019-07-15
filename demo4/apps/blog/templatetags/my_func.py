from django.template import library
from blog.models import Article
register=library.Library()

@register.simple_tag
def getlatestarticles(num=3):
    return Article.objects.order_by('-create_time')[:num]

@register.filter
def mylower(value):
    return value.lower()