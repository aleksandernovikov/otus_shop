from django.urls import path

from products.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index')
]
