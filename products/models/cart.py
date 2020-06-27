from decimal import Decimal

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import F, Sum, Count, DecimalField
from django.utils.translation import gettext_lazy as _

from ..models.product import Product

User = get_user_model()


class CartProduct(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_products')
    product = models.ForeignKey(Product, related_name='in_cart', on_delete=models.CASCADE)
    count = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'{self.product} x {self.count}'

    @staticmethod
    def cart_products_minimal(user):
        result = {'total': 0, 'count': 0}
        if user.is_authenticated:
            result = CartProduct.objects.filter(owner=user).select_related('product') \
                .aggregate(
                total=Sum(F('product__price') * F('count'), output_field=DecimalField()),
                count=Count('id')
            )
            result['total'] = result.get('total') if result['total'] else 0
            return result
        return result

    @staticmethod
    def empty_cart(user):
        CartProduct.objects.filter(owner=user).delete()

    class Meta:
        verbose_name = _('Cart Product')
        verbose_name_plural = _('Cart Products')
