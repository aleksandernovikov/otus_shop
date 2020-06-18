from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='usability/pages/blog.html'), name='blog'),
    path('post/', TemplateView.as_view(template_name='usability/pages/post.html'), name='post'),
]
