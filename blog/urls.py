from django.urls import path

from .views import BlogRootListView, BlogCategoryListView, BlogPostView

urlpatterns = [
    path('', BlogRootListView.as_view(), name='blog'),
    path('<slug:slug>/', BlogCategoryListView.as_view(), name='blog-category'),
    path('post/<slug:slug>/', BlogPostView.as_view(), name='single-post'),
]
