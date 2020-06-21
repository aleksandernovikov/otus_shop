from django.contrib.auth import get_user_model
from django.db import models
from django.utils.functional import cached_property
from easy_thumbnails.fields import ThumbnailerImageField
from pytils.translit import slugify
from django.utils.translation import gettext_lazy as _
from treebeard.mp_tree import MP_Node

from reference.models import Characteristic

User = get_user_model()


class ProductCategory(MP_Node):
    """
    Категория товара
    """
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(blank=True)

    image = ThumbnailerImageField(upload_to='shop_categories', blank=True)
    description = models.TextField(_('Category description'), blank=True)

    show_in_top = models.BooleanField(_('Show in top'), default=True)
    show_in_sidebar = models.BooleanField(_('Show in sidebar'), default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Product category')
        verbose_name_plural = _('Product categories')

    def save(self, *args, **kwargs):
        """
        add slug
        :param args:
        :param kwargs:
        :return:
        """
        if not self.pk and not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class ProductImage(models.Model):
    product = models.ForeignKey('Product', related_name='product_images', on_delete=models.CASCADE)
    image = ThumbnailerImageField(upload_to='products')
    order = models.PositiveSmallIntegerField(default=0, db_index=True)

    def __str__(self):
        return self.image.url

    class Meta:
        ordering = ('order',)


class Product(models.Model):
    """
    Товар
    """
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(blank=True, unique=True)

    description = models.TextField(blank=True)

    price = models.DecimalField(decimal_places=2, max_digits=5)
    sale_price = models.DecimalField(_('Sale price'),
                                     decimal_places=2, max_digits=5,
                                     blank=True,
                                     null=True,
                                     help_text='Discount price')

    images = models.ManyToManyField(ProductImage, related_name='products')

    @cached_property
    def main_image(self):
        i = self.product_images.first()
        return i.image

    @property
    def discount_percent(self):
        percent = self.sale_price / self.price
        return round((1 - percent) * 100)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk and not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

# class ProductVariant(models.Model):
#     """
#     Вариант товара (размер, цвет, длина)
#     """
#     parent_product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     title = models.CharField(max_length=30)
#
#     characteristics = models.ManyToManyField(
#         Characteristic,
#         blank=True,
#         through='ProductVariantCharacteristic'
#     )
#
#     def __str__(self):
#         return f'{self.parent_product} -> {self.title}'
#
#
# class ProductVariantCharacteristic(models.Model):
#     """
#     Характеристики варианта конкретного товара
#     """
#     product_variant = models.ForeignKey(
#         ProductVariant,
#         related_name='variant_characteristic',
#         on_delete=models.CASCADE
#     )
#     characteristic = models.ForeignKey(Characteristic, on_delete=models.CASCADE)
#     value = models.IntegerField(default=0)
#
#     class Meta:
#         unique_together = 'product_variant', 'characteristic'
#
#     def __str__(self):
#         return f'{self.characteristic}: {self.value}'
