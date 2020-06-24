from rest_framework import serializers

from products.models.cart import CartProduct
from products.models.product import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'title', 'price',


class ShortCartProductSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = CartProduct
        fields = 'owner', 'product', 'id', 'count'


class DefaultCartProductSerializer(ShortCartProductSerializer):
    product = ProductSerializer()
