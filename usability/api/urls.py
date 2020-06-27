from rest_framework.routers import DefaultRouter

from .views import SubscriberViewSet, AdminMessageViewSet, FavoriteProductViewSet

api_router = DefaultRouter()
api_router.register('subscribe', SubscriberViewSet, basename='subscribe')
api_router.register('leave-message', AdminMessageViewSet, basename='leave-message')
api_router.register('favorite', FavoriteProductViewSet, basename='favorite')

urlpatterns = api_router.urls
