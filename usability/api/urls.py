from rest_framework.routers import DefaultRouter

from .views import SubscriberViewSet, AdminMessageViewSet

api_router = DefaultRouter()

api_router.register('subscribe', SubscriberViewSet, basename='subscribe')
api_router.register('leave-message', AdminMessageViewSet, basename='leave-message')

urlpatterns = api_router.urls
