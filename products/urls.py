from django.urls import path

from products.views import ShopRootListView, ShopCategoryListView, ProductDetails

urlpatterns = [
    path('', ShopRootListView.as_view(), name='shop'),
    path('<slug:slug>/', ShopCategoryListView.as_view(), name='shop-category'),
    path('product/<slug:slug>/', ProductDetails.as_view(), name='product-details'),
]
