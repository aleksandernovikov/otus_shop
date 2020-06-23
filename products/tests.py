from rest_framework import status
from rest_framework.test import APITestCase

from products.models.product import Product
from shop_user.models import ShopUser


class TestApiCartProducts(APITestCase):
    fixtures = ['user', 'product_categories', 'products']

    def setUp(self) -> None:
        self.base_url = '/api/cart-products/'
        self.user = ShopUser.objects.first()

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

    # def test_remove_from_cart(self):
