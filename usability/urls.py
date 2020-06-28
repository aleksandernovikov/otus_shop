from django.urls import path
from django.views.generic import TemplateView

from .views import FavoriteProductView

urlpatterns = [
    path('', TemplateView.as_view(template_name='usability/pages/index.html'), name='index'),
    path('contacts/', TemplateView.as_view(template_name='usability/pages/contacts.html'), name='contacts'),
    path('favorites/', FavoriteProductView.as_view(), name='favorites'),
]
