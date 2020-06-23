from rest_framework.routers import DefaultRouter

from products.api.views import  CartProductViewSet

api_router = DefaultRouter()

api_router.register('cart-products', CartProductViewSet, basename='cart-products')

urlpatterns = api_router.urls
