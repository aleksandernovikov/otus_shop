from django.contrib.auth import get_user_model
from django.db import models

from products.models import Product

User = get_user_model()


class Cart(models.Model):
    """
    Корзина
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'{self.user} -> {self.product} x {self.count}'
