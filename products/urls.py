from django.urls import path

from products.views import ShopRootListView, ShopCategoryListView

urlpatterns = [
    path('', ShopRootListView.as_view(), name='shop'),
    path('<slug:slug>/', ShopCategoryListView.as_view(), name='shop-category')
]
