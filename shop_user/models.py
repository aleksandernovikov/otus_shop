from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from easy_thumbnails.fields import ThumbnailerImageField


class ShopUser(AbstractUser):
    avatar = ThumbnailerImageField(upload_to='avatars', blank=True)
    short_description = models.CharField(_('Short Description'), max_length=30, blank=True)

    middle_name = models.CharField(_('Middle Name'), max_length=100, blank=True)

    email = models.EmailField(_('email address'), blank=True, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    @property
    def display_name(self):
        full_name = f'{self.first_name} {self.last_name}'
        return full_name if full_name else self.username

    def __str__(self):
        return self.display_name
