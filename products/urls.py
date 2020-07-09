from django.urls import path

from products.views.product_details import ProductDetailsView
from .views.shop_list import ShopListView

urlpatterns = [
    path('', ShopListView.as_view(), name='shop'),
    path('<slug:slug>/', ShopListView.as_view(), name='shop-category'),
    path('product/<slug:slug>/', ProductDetailsView.as_view(), name='product-details'),
]
