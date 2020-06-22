from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from pytils.translit import slugify
from treebeard.mp_tree import MP_Node
from django.utils.translation import gettext_lazy as _


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
