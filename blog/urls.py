from django.urls import path
from django.views.generic import TemplateView

from .views import BlogRootListView, BlogCategoryListView, BlogPostView

urlpatterns = [
    # path('', TemplateView.as_view(template_name='usability/pages/blog.html'), name='blog'),
    path('', BlogRootListView.as_view(), name='blog'),
    path('<slug:slug>/', BlogCategoryListView.as_view(), name='blog_category'),
    # path('post/<slug:slug>/', TemplateView.as_view(template_name='usability/pages/post.html'), name='post'),
    path('post/<slug:slug>/', BlogPostView.as_view(), name='single-post'),
]
