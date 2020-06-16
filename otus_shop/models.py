from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class ProductCategory(models.Model):
    """
    Категория товара
    """
    title = models.CharField(max_length=100)


class Product(models.Model):
    """
    Товар
    """
    title = models.CharField(max_length=100)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveSmallIntegerField(default=1)
