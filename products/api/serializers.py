from rest_framework import serializers

from products.models.cart import CartProduct
from products.models.product import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'title', 'price',


class CartProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartProduct
        fields = 'product', 'count'


# class CartSerializer(serializers.ModelSerializer):
#     owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
#     products = ProductSerializer(many=True)
#
#     class Meta:
#         model = Cart
#         read_only_fields = 'owner',
#         fields = 'owner', 'products',
