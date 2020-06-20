from django import views

from products.models import Product


class ShopRootListView(views.generic.ListView):
    model = Product
    template_name = 'usability/pages/shop.html'


class ShopCategoryListView(views.generic.ListView):
    model = Product
    template_name = 'usability/pages/shop.html'
