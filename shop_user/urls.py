from django.urls import path, include

from shop_user.views import ShopUserProfile

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/', ShopUserProfile.as_view(), name='user-profile'),
]
