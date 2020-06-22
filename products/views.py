from django import views
from django.db.models import Sum, DecimalField

from products.models.cart import CartProduct
from .models.product_category import ProductCategory
from .models.product import Product


class ShopRootListView(views.generic.ListView):
    model = Product
    template_name = 'usability/pages/shop.html'


class ShopCategoryListView(views.generic.ListView):
    model = Product
    template_name = 'usability/pages/shop.html'

    def get_queryset(self):
        category_slug = self.kwargs.get('slug')
        return self.model.objects.filter(category__slug=category_slug)

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)

        ctx.update({
            'category': ProductCategory.objects.get(slug=self.kwargs.get('slug'))
        })
        return ctx


class ProductDetails(views.generic.DetailView):
    model = Product
    template_name = 'usability/pages/product_details.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(**kwargs)
        product = self.get_object()

        ctx.update({
            'product_images': product.product_images.all()
        })
        return ctx


class CartProductView(views.generic.TemplateView):
    template_name = 'usability/pages/cart.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(**kwargs)

        from django.db.models import F
        # filter(owner=self.request.user).
        total = Sum(F('count')*F('product__price'), output_field=DecimalField)
        cart_products = CartProduct.objects.aggregate(
            total=total
        )

        ctx.update({
            'cart_products': cart_products
        })
        return ctx
