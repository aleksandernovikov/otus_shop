from django.db.models import F, Sum, DecimalField

from .models.cart import CartProduct
from .models.order import OrderedProduct


def get_cart_products_max(user):
    """
    Товары из корзины с максимумом информации
    """
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


def get_cart_products_min(user):
    """
    Товары из корзины с минимумом информации
    """
    return CartProduct.objects.filter(
        owner=user
    ).select_related('product').values(
        'count',
        'product_id'
    ).annotate(
        title=F('product__title'),
        price=F('product__price'),
        total=Sum(F('product__price') * F('count'), output_field=DecimalField())
    )


def add_products_to_order(products, order_id):
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
