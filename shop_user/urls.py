from django.urls import path, include

from shop_user.views import ShopUserProfile, ShopUserSignUp, OrderListView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/', ShopUserProfile.as_view(), name='user-profile'),
    path('signup/', ShopUserSignUp.as_view(), name='user-signup'),
    path('orders/', OrderListView.as_view(), name='user-orders')
]
