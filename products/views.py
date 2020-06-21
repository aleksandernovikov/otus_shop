from django import views

from products.models import Product


class ShopRootListView(views.generic.ListView):
    model = Product
    template_name = 'usability/pages/shop.html'


class ShopCategoryListView(views.generic.ListView):
    model = Product
    template_name = 'usability/pages/shop.html'


class ProductDetails(views.generic.DetailView):
    model = Product
    template_name = 'usability/pages/product_details.html'
