from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from ..models.product import Product

User = get_user_model()


class CartProduct(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_products')
    product = models.ForeignKey(Product, related_name='in_cart', on_delete=models.CASCADE)
    count = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'{self.product} x {self.count}'

    class Meta:
        verbose_name = _('Cart Product')
        verbose_name_plural = _('Cart Products')