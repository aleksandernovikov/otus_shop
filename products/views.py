from django import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum, DecimalField, Value
from django.db.models import F

from .models.cart import CartProduct
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


class CartProductView(LoginRequiredMixin, views.generic.TemplateView):
    """
    Вывод корзины с товарами
    # TODO: нужно переделать
    """
    template_name = 'usability/pages/cart.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(**kwargs)

        cart_products = CartProduct.objects.filter(
            owner=self.request.user
        ).select_related(
            'product'
        ).values(
            'count',
        ).annotate(
            cart_product_id=F('id'),
            slug=F('product__slug'),
            product_id=F('product__id'),
            title=F('product__title'),
            price=F('product__price'),
        )

        cart_products_ids = [product.get('product_id') for product in cart_products]
        products = Product.objects.filter(pk__in=set(cart_products_ids)).prefetch_related('images')

        images_dict = {}
        for product in products:
            images_dict[product.id] = product.main_image

        full_cart_products = [{
            **p,
            'image': images_dict.get(p.get('product_id')),
            'total': p.get('count') * p.get('price')
        } for p in cart_products]

        total = sum([product.get('total') for product in full_cart_products])

        ctx.update({
            'cart_products': full_cart_products,
            'total': total
        })
        return ctx
