from rest_framework import serializers

from ..models.cart import CartProduct
from ..models.product import Product


class ShortProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'title', 'price',


class ShortCartProductSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = CartProduct
        fields = 'owner', 'product', 'id', 'count'


class DefaultCartProductSerializer(ShortCartProductSerializer):
    product = ShortProductSerializer()
