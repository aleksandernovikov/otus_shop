from django.contrib.auth import get_user_model
from django.db import models
from treebeard.mp_tree import MP_Node

User = get_user_model()


class ProductCategory(MP_Node):
    """
    Категория товара
    """
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Product(models.Model):
    """
    Товар
    """
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Cart(models.Model):
    """
    Корзина
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'{self.user} -> {self.product} x {self.count}'
