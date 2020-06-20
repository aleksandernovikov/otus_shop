from django.urls import path

from shop_user.views import ShopUserProfile

urlpatterns = [
    path('profile/', ShopUserProfile.as_view(), name='user-profile'),
]
