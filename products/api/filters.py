from django_filters.rest_framework import FilterSet, RangeFilter

from ..models.product import Product


class ProductFilter(FilterSet):
    price = RangeFilter(field_name="price")

    class Meta:
        model = Product
        fields = 'category', 'price'
