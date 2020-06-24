from rest_framework import status
from rest_framework.test import APITestCase

from products.models.cart import CartProduct
from products.models.product import Product
from shop_user.models import ShopUser


class TestApiCartProducts(APITestCase):
    fixtures = ['user', 'product_categories', 'products']

    def setUp(self) -> None:
        self.base_url = '/api/cart-products/'
        self.user = ShopUser.objects.first()

    @staticmethod
    def _add_to_cart(user, product, count):
        CartProduct.objects.create(owner=user, product=product, count=count)

    def test_add_to_cart(self):
        product = Product.objects.first()
        count = 2
        self.client.force_login(self.user)

        response = self.client.post(self.base_url, {
            'product': product.id,
            'count': count
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.get(self.base_url)
        cart_data = response.json()

        cart_product = cart_data[0].get('product')
        self.assertEqual(cart_product.get('title'), product.title)
        self.assertEqual(cart_product.get('price'), str(product.price))
        self.assertEqual(cart_data[0].get('count'), count)

    def test_cart_minimal_information(self):
        product = Product.objects.first()
        product_count = 3
        self._add_to_cart(self.user, product, count=product_count)
        self.client.force_login(self.user)
        response = self.client.get(self.base_url + 'count/')

        cart = response.json()
        self.assertEqual(cart.get('count'), 1)
        self.assertEqual(cart.get('total'), product.price * product_count)
