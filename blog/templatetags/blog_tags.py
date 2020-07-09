from typing import Optional

from django import template
from django.db.models import Count, QuerySet
from django.template import RequestContext

from ..models import PostCategory, Post

register = template.Library()


@register.inclusion_tag('tags/blog_categories.html')
def post_categories() -> dict:
    categories: QuerySet = PostCategory.objects.values('title', 'slug').annotate(cnt=Count('posts'))
    return {
        'categories': categories
    }


@register.inclusion_tag('tags/related_posts.html', takes_context=True)
def related_posts(context: RequestContext, title: str) -> dict:
    """
    Похожие публикации
    """
    posts: QuerySet = Post.objects.values('publication_date', 'title', 'slug', 'image', 'text')

    post_slug: Optional[str] = context.request.resolver_match.kwargs.get('slug')
    if post_slug:
        posts = posts.exclude(slug=post_slug)

    return {
        'title': title,
        'related_posts': posts[:3]
    }
