from django.contrib.auth import get_user_model
from django.db import models
from treebeard.mp_tree import MP_Node

User = get_user_model()


class ProductCategory(MP_Node):
    """
    Категория товара
    """
    title = models.CharField(max_length=100)
    show_subcategory_products = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = 'title', 'depth'


class Product(models.Model):
    """
    Товар
    """
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class ProductVariant(models.Model):
    """
    Вариант товара (размер, цвет, длина)
    """
    parent_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)

    characteristics = models.ManyToManyField(
        'Characteristic',
        blank=True,
        through='ProductVariantCharacteristic'
    )

    def __str__(self):
        return f'{self.parent_product} -> {self.title}'


class Measure(models.Model):
    """
    Единица измерения
    """
    title = models.CharField(max_length=50, unique=True)
    short_title = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.title


class Characteristic(models.Model):
    """
    Характеристика товара
    """
    title = models.CharField(max_length=100, unique=True)
    short_title = models.CharField(max_length=50, unique=True)
    measure = models.ForeignKey(Measure, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ProductVariantCharacteristic(models.Model):
    """
    Характеристики варианта конкретного товара
    """
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    characteristic = models.ForeignKey(Characteristic, on_delete=models.CASCADE)
    value = models.IntegerField(default=0)

    class Meta:
        unique_together = 'product_variant', 'characteristic'

    def __str__(self):
        return f'{self.characteristic}: {self.value}'


class Cart(models.Model):
    """
    Корзина
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'{self.user} -> {self.product} x {self.count}'
