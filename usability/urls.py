from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='usability/pages/index.html'), name='index'),
    path('contacts/', TemplateView.as_view(template_name='usability/pages/contacts.html'), name='contacts'),
    path('cart/', TemplateView.as_view(template_name='usability/pages/cart.html'), name='cart'),
    path('checkout/', TemplateView.as_view(template_name='usability/pages/checkout.html'), name='checkout'),
]
