from django.db import models
from django.utils.functional import cached_property
from pytils.translit import slugify
from django.utils.translation import gettext_lazy as _

from products.models.product_category import ProductCategory
from products.models.product_image import ProductImage


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
        m = _('at a price of')
        from django.conf import settings
        return f'{self.title} {m} {self.price} {settings.SITE_DATA.get("currency")}'

    def save(self, *args, **kwargs):
        if not self.pk and not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
