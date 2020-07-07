from django.db import models
from django.utils.functional import cached_property
from pytils.translit import slugify
from django.utils.translation import gettext_lazy as _

from .product_category import ProductCategory
from .product_image import ProductImage


class Product(models.Model):
    """
    Product model
    """
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(blank=True, unique=True)

    description = models.TextField(_('description'), blank=True)

    price = models.DecimalField(_('Selling price'), decimal_places=2, max_digits=9,
                                help_text=_('Price at which the product will be sold'))

    characteristics = models.ManyToManyField('ProductMeasure', through='ProductCharacteristic', blank=True,
                                             verbose_name=_('Product Characteristics'))

    strikeout_price = models.DecimalField(_('Strikeout price'),
                                          decimal_places=2, max_digits=5,
                                          blank=True,
                                          null=True,
                                          help_text=_('Crossed/old product price')
                                          )

    images = models.ManyToManyField(ProductImage, related_name='products')

    sort_order = models.PositiveSmallIntegerField(_('Ordering'), default=0)

    @cached_property
    def main_image(self):
        i = self.product_images.first()
        return i.image

    @property
    def discount_percent(self):
        """
        Процент скидки
        :return:
        """
        percent = self.price / self.strikeout_price
        return round((1 - percent) * 100)

    def __str__(self):
        m = _('at a price of')
        from django.conf import settings
        return f'{self.title} {m} {self.price} {settings.SITE_DATA.get("currency")}'

    def save(self, *args, **kwargs):
        """
        Автогенерация слага
        :param args:
        :param kwargs:
        :return:
        """
        if not self.pk and not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        ordering = ('-sort_order',)
