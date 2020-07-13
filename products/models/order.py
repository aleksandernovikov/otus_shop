import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from products.models.product import Product

User = get_user_model()


class Order(models.Model):
    """
    Order model
    """
    ORDER_CREATED = 1
    ORDER_AWAITING_PAYMENT = 2
    ORDER_PAID = 3
    ORDER_PROCESSED = 4
    ORDER_SHIPPED = 5
    ORDER_CANCELLED = 6

    ORDER_STATUS = (
        (ORDER_CREATED, _('Created')),
        (ORDER_AWAITING_PAYMENT, _('Awaiting payment')),
        (ORDER_PAID, _('Paid')),
        (ORDER_PROCESSED, _('Order is ready for delivery')),
        (ORDER_SHIPPED, _('Order shipped')),
        (ORDER_CANCELLED, _('Order cancelled'))
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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

    order_created = models.DateTimeField(_('Order created'), auto_now_add=True, editable=False, blank=True)
    order_updated = models.DateTimeField(_('Order updated'), auto_now=True, blank=True)

    order_status = models.PositiveSmallIntegerField(_('Order status'), choices=ORDER_STATUS, default=ORDER_CREATED)

    products = models.ManyToManyField(Product, through='OrderedProduct')
    total_order_price = models.DecimalField(decimal_places=2, max_digits=9)

    def __str__(self):
        return f'{self.user} {self.order_created}'


class OrderedProduct(models.Model):
    """
    Продукты заказа, в них запоминаеются заказ, продукт, цена продукта и количество
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='ordered_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    selling_price = models.DecimalField(max_digits=9, decimal_places=2)
    count = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.order}->{self.product}'
