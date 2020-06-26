from django.urls import path

from products.views import ShopRootListView, ShopCategoryListView, ProductDetailsView

urlpatterns = [
    path('', ShopRootListView.as_view(), name='shop'),
    path('<slug:slug>/', ShopCategoryListView.as_view(), name='shop-category'),
    path('product/<slug:slug>/', ProductDetailsView.as_view(), name='product-details'),
]
