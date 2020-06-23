from products.models.cart import CartProduct


def cart_data(request):
    count = CartProduct.cart_products_count(request.user)
    return {
        'products_in_cart': count
    }
