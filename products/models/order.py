from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from products.models.product import Product

User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    first_name = models.CharField(_('First Name'), max_length=70)
    last_name = models.CharField(_('Last Name'), max_length=70)

    state = models.CharField(_('State'), max_length=100)
    city = models.CharField(_('City'), max_length=70)

    street = models.CharField(_('Street'), max_length=70)
    building = models.CharField(_('Building'), max_length=50)

    phone = models.CharField(_('Phone'), max_length=12)
    post_code = models.CharField(_('Post Code'), max_length=20, blank=True)

    customer_notes = models.CharField(_('Customer Notes'), max_length=250, blank=True)
    manager_notes = models.CharField(_('Manager Notes'), max_length=250, blank=True)

    order_date = models.DateTimeField(auto_now=True)
    products = models.ManyToManyField(Product)
    total_order_price = models.DecimalField(decimal_places=2, max_digits=7)


class OrderedProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ordered_products')
    selling_price = models.DecimalField(max_digits=7, decimal_places=2)
    count = models.PositiveSmallIntegerField()
