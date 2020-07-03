from django import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy

from .forms import OrderForm
from .models.cart import CartProduct
from .models.order import Order
from .models.product_category import ProductCategory
from .models.product import Product
from .services import (
    get_cart_products_max,
    add_products_to_order
)


class ShopMixin:
    """
    Базовый миксин для просмотра товаров магазина
    """
    model = Product
    template_name = 'usability/pages/shop.html'
    paginate_by = 6
    allowed_sort_params = ('price', '-price')

    def get_queryset(self):
        """
        Сортровки на страницах магазина
        """
        sort_param = self.request.GET.get('sort')
        queryset = self.model.objects.all()

        if sort_param in self.allowed_sort_params:
            return queryset.order_by(sort_param)

        return queryset

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        sort_param = self.request.GET.get('sort')
        if sort_param in self.allowed_sort_params:
            ctx.update({
                'current_sorting': sort_param
            })
        return ctx


class ShopRootListView(ShopMixin, views.generic.ListView):
    def get_queryset(self):
        return super().get_queryset().prefetch_related('product_images')


class ShopCategoryListView(ShopMixin, views.generic.ListView):
    """
    Просмотр категории товаров
    """

    def get_queryset(self):
        category_slug = self.kwargs.get('slug')
        return super().get_queryset().filter(
            category__slug=category_slug
        ).prefetch_related('product_images')

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)

        try:
            slug = self.kwargs.get('slug')
            ctx.update({
                'category': ProductCategory.objects.get(slug=slug)
            })
        except ProductCategory.DoesNotExist:
            raise Http404

        return ctx


class ProductDetailsView(views.generic.DetailView):
    """
    Страница товара
    """
    model = Product
    template_name = 'usability/pages/product_details.html'

    def get_context_data(self, *args, **kwargs):
        """
        Пробросим данные о фотографиях товара, чтобы не делать запрос в шаблоне
        """
        ctx = super().get_context_data(**kwargs)
        product = self.get_object()

        ctx.update({
            'product_images': product.product_images.all(),
            'product_characteristics': product.product_characteristics.all()
        })
        return ctx


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
