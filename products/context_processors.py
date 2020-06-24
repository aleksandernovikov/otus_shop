from products.models.cart import CartProduct


def cart_data(request):
    cart = CartProduct.cart_products_minimal(request.user)
    return {
        'products_in_cart': cart.get('count', 0),
        'cart_total': cart.get('total', 0)
    }
