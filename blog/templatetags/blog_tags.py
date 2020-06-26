from django import template
from django.db.models import Count

from ..models import PostCategory, Post

register = template.Library()


@register.inclusion_tag('tags/blog_categories.html')
def post_categories():
    categories = PostCategory.objects.values('title', 'slug').annotate(cnt=Count('posts'))
    return {
        'categories': categories
    }


@register.inclusion_tag('tags/related_posts.html', takes_context=True)
def related_posts(context, title):
    """
    Похожие публикации
    """
    post_slug = context.request.resolver_match.kwargs.get('slug')
    posts = Post.objects.exclude(slug=post_slug).values('publication_date', 'title', 'slug', 'image', 'text')

    return {
        'title': title,
        'related_posts': posts[:3]
    }
