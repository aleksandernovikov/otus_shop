from django.urls import path
from rest_framework.routers import DefaultRouter

from products.api.views import CartProductViewSet, ProductList

api_router = DefaultRouter()

api_router.register('cart-products', CartProductViewSet, basename='cart-products')

urlpatterns = [
                  path('products/', ProductList.as_view(), name='products'),
              ] + api_router.urls
