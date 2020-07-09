from random import sample

from django.db.models import QuerySet

from products.models.product import Product
from .models.cart import CartProduct
from .models.order import OrderedProduct


def get_cart_products_max(user):
    """
    Products from the cart with a maximum of information
    """
    # everything below is done due to the model property main_image
    cart_products = CartProduct.objects.filter(
        owner=user
    ).select_related(
        'product'
    ).prefetch_related(
        'product__images'
    )

    result = [{
        'cart_product_id': cart_product.id,
        'slug': cart_product.product.slug,
        'product_id': cart_product.product.id,
        'title': cart_product.product.title,
        'price': cart_product.product.price,
        'count': cart_product.count,
        'image': cart_product.product.main_image,
        'total': cart_product.product.price * cart_product.count,
    } for cart_product in cart_products]

    return result


def add_products_to_order(products, order_id: int):
    """
    Свяжем продукты корзины с заказом
    """
    ordered_products = [OrderedProduct(
        order_id=order_id,
        product_id=cart_product.get('product_id'),
        selling_price=cart_product.get('price'),
        count=cart_product.get('count')
    ) for cart_product in products]

    OrderedProduct.objects.bulk_create(ordered_products)


def find_related_products(parent_product_id: int = None, sample_size: int = 4) -> QuerySet:
    """
    the simplest algorithm for selecting related products
    Separated logic for convenience changes
    """

    all_products_list = list(Product.objects.values_list('id', flat=True))
    random_product_ids = sample(all_products_list, min(len(all_products_list), sample_size + 1))

    return Product.objects.filter(id__in=random_product_ids).exclude(
        id=parent_product_id
    ).select_related('category').prefetch_related('product_images')[:sample_size]
