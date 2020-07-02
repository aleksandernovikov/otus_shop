from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import F, Sum, Count, DecimalField
from django.utils.translation import gettext_lazy as _

from ..models.product import Product

User = get_user_model()


class ProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related('product')

    def minimal_output(self, user):
        return self.get_queryset().filter(owner=user).values(
            'count', 'product_id'
        ).annotate(
            title=F('product__title'),
            price=F('product__price'),
            total=Sum(F('product__price') * F('count'), output_field=DecimalField())
        )


class CartProduct(models.Model):
    """
    Product in cart
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_products')
    product = models.ForeignKey(Product, related_name='in_cart', on_delete=models.CASCADE)
    count = models.PositiveSmallIntegerField(default=1)
    objects = models.Manager()
    products = ProductManager()

    def __str__(self):
        return f'{self.product} x {self.count}'

    @staticmethod
    def cart_products_minimal(user):
        """
        Used in the context processor on each page,
        to show the amount and quantity of products in the cart
        """
        result = {'total': 0, 'count': 0}
        if user.is_authenticated:
            result = CartProduct.products.filter(owner=user) \
                .aggregate(
                total=Sum(F('product__price') * F('count'), output_field=DecimalField()),
                count=Count('id')
            )
            result['total'] = result.get('total') if result['total'] is not None else 0
            return result
        return result

    @staticmethod
    def empty_cart(user):
        """
        Empty the cart
        """
        CartProduct.objects.filter(owner=user).delete()

    class Meta:
        verbose_name = _('Cart Product')
        verbose_name_plural = _('Cart Products')
