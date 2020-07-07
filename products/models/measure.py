from django.db import models
from django.utils.translation import gettext_lazy as _


class ProductMeasure(models.Model):
    """
    Measure unit
    """
    NOT_SELECTED = 0
    MEASURE_WEIGHT = 1
    MEASURE_QUANTITY = 2
    MEASURE_LENGTH = 3

    MEASURE_CATEGORIES = (
        (NOT_SELECTED, _('Measure category is not selected')),
        (MEASURE_WEIGHT, _('Weight')),
        (MEASURE_QUANTITY, _('Quantity')),
        (MEASURE_LENGTH, _('Length'))
    )

    title = models.CharField(_('Measure name'), max_length=10)
    category = models.PositiveSmallIntegerField(_('Measure Category'), default=0, choices=MEASURE_CATEGORIES)

    def __str__(self):
        return f'{self.title}, {self.get_category_display()}'


class ProductCharacteristic(models.Model):
    """
    Product characteristic
    """
    product = models.ForeignKey('Product', related_name='product_characteristics', on_delete=models.CASCADE)
    measure = models.ForeignKey(ProductMeasure, on_delete=models.CASCADE)
    value = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'{self.measure.get_category_display()}: {self.value} {self.measure.title}'
