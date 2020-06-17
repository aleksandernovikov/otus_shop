from django.contrib.auth import get_user_model
from django.db import models
from treebeard.mp_tree import MP_Node

from reference.models import Characteristic
from usability.models import ProductCategory

User = get_user_model()


class Product(models.Model):
    """
    Товар
    """
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class ProductVariant(models.Model):
    """
    Вариант товара (размер, цвет, длина)
    """
    parent_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)

    characteristics = models.ManyToManyField(
        Characteristic,
        blank=True,
        through='ProductVariantCharacteristic'
    )

    def __str__(self):
        return f'{self.parent_product} -> {self.title}'


class ProductVariantCharacteristic(models.Model):
    """
    Характеристики варианта конкретного товара
    """
    product_variant = models.ForeignKey(
        ProductVariant,
        related_name='variant_characteristic',
        on_delete=models.CASCADE
    )
    characteristic = models.ForeignKey(Characteristic, on_delete=models.CASCADE)
    value = models.IntegerField(default=0)

    class Meta:
        unique_together = 'product_variant', 'characteristic'

    def __str__(self):
        return f'{self.characteristic}: {self.value}'
