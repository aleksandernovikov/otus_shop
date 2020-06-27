from django.db import models
from django.utils.translation import gettext_lazy as _


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
        verbose_name = _('Admin Message')
        verbose_name_plural = _('Admin Messages')
        unique_together = ('message', 'ip')

    def __str__(self):
        return f'{self.name} {self.created}'
