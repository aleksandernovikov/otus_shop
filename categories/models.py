from django.db import models
from django.utils.translation import gettext_lazy as _
from pytils.translit import slugify
from treebeard.mp_tree import MP_Node


class ProductCategory(MP_Node):
    """
    Категория товара
    """
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Post category')
        verbose_name_plural = _('Post categories')

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
