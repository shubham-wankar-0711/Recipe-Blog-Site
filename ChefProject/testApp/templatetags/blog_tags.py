from testApp.models import Post
from django.template import Library

register = Library()

@register.simple_tag(name='my_tag')
def total_posts():
    return Post.objects.count()

@register.inclusion_tag('testApp/latest_posts.html')
def show_latest_posts(count=3):
    latest_posts = Post.objects.order_by('-publish')[:count]
    return {'latest_posts':latest_posts}

from django.db.models import Count

@register.simple_tag()
def get_most_commented_posts(count=4):
    return Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]
