from django import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy

from products.forms import OrderForm
from products.models.cart import CartProduct
from products.models.order import Order
from products.models.product_category import ProductCategory
from products.models.product import Product
from products.services import (
    get_cart_products_max,
    add_products_to_order
)


class CartProductView(LoginRequiredMixin, views.generic.TemplateView):
    """
    Products from the cart
    """
    template_name = 'usability/pages/cart.html'

    def get_context_data(self, *args, **kwargs):
        """
        на странице корзины нужна информация
        о заказанных продуктах и сумме заказа
        """
        ctx = super().get_context_data(**kwargs)
        full_cart_products = get_cart_products_max(self.request.user)
        total = sum([product.get('total') for product in full_cart_products])

        ctx.update({
            'cart_products': full_cart_products,
            'total': total
        })
        return ctx


class OrderCreateView(LoginRequiredMixin, views.generic.CreateView):
    """
    Создание заказа
    """
    model = Order
    template_name = 'usability/pages/checkout.html'
    form_class = OrderForm
    success_url = reverse_lazy('shop')

    def get_context_data(self, **kwargs):
        """
        on the form you need information about the ordered products and the order amount
        """
        ctx = super().get_context_data(**kwargs)
        ctx.update({
            'cart_products': CartProduct.products.minimal_output(self.request.user)
        })
        return ctx

    def get_initial(self):
        """
        Fill out the form with the available data.
        """
        initial = super().get_initial()
        try:
            latest_order = Order.objects.latest('order_created')
            initial.update({
                'first_name': latest_order.first_name,
                'last_name': latest_order.last_name,
                'state': latest_order.state,
                'city': latest_order.city,
                'street': latest_order.street,
                'building': latest_order.building,
                'phone': latest_order.phone,
                'post_code': latest_order.post_code
            })
            return initial
        except Order.DoesNotExist:
            initial.update({
                'first_name': self.request.user.first_name,
                'last_name': self.request.user.last_name,
            })
            return initial

    def form_valid(self, form):
        """
        Creates a snapshot of the order and then empties the cart.
        """
        cart_products = CartProduct.products.minimal_output(self.request.user)

        new_form = form.save(commit=False)
        new_form.user = self.request.user
        new_form.total_order_price = sum(
            [product.get('total') for product in cart_products]
        )
        new_form.save()

        # create snapshot
        add_products_to_order(cart_products, new_form.pk)
        # empty the cart
        CartProduct.empty_cart(self.request.user)

        return super().form_valid(form)
