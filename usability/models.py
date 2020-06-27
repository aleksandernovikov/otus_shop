from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from products.models.product import Product

User = get_user_model()


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('Subscriber')
        verbose_name_plural = _('Subscribers')

    def __str__(self):
        return self.email


class AdminMessage(models.Model):
    name = models.CharField(_('Name'), max_length=70)
    email = models.EmailField(_('Email'))
    message = models.TextField(_('Message'), max_length=1000)
    created = models.DateTimeField(auto_now=True, blank=True)
    ip = models.GenericIPAddressField(_('Ip'))

    class Meta:
        ordering = 'created',
        unique_together = ('message', 'ip')
        verbose_name = _('Admin Message')
        verbose_name_plural = _('Admin Messages')

    def __str__(self):
        return f'{self.name}<{self.email}> {self.created:%Y-%m-%d %H:%M}'


class FavoriteProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Favorite Product')
        verbose_name_plural = _('Favorite Products')

    def __str__(self):
        return f'{self.user} {self.product}'
