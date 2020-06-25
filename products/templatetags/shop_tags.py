from django import template

from ..models.product import Product
from ..models.product_category import ProductCategory

register = template.Library()


@register.inclusion_tag('tags/shop_categories.html')
def shop_categories(place):
    place_name = 'show_in_top' if place == 'top' else 'show_in_sidebar'
    categories = ProductCategory.objects.filter(**{place_name: True})

    return {
        'categories': categories
    }


@register.inclusion_tag('tags/sale_products.html')
def sale_block(max_count=6):
    products = Product.objects.filter(strikeout_price__isnull=False)[:max_count]

    return {
        'sale_products': products
    }


@register.inclusion_tag('tags/shop_categories_carousel.html')
def shop_categories_carousel():
    categories = ProductCategory.objects.filter(image__isnull=False)[:8]

    return {
        'categories': categories
    }
