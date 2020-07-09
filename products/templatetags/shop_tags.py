from django import template
from django.conf import settings
from django.db.models import QuerySet
from treebeard.mp_tree import MP_NodeQuerySet

from products.services import find_related_products
from ..models.product import Product
from ..models.product_category import ProductCategory

register = template.Library()


@register.inclusion_tag('tags/shop_categories.html')
def shop_categories(place: str) -> dict:
    place_name: str = 'show_in_top' if place == 'top' else 'show_in_sidebar'
    categories: MP_NodeQuerySet = ProductCategory.objects.filter(**{place_name: True}).values('title', 'slug')

    return {
        'categories': categories
    }


@register.inclusion_tag('tags/sale_products.html')
def sale_block(max_count: int = 6) -> dict:
    products: QuerySet = Product.objects.filter(strikeout_price__isnull=False).prefetch_related(
        'product_images'
    ).select_related(
        'category'
    )[:max_count]

    return {
        'sale_products': products,
        'site': settings.SITE_DATA
    }


@register.inclusion_tag('tags/shop_categories_carousel.html')
def shop_categories_carousel(carousel_size: int = 8) -> dict:
    categories: QuerySet = ProductCategory.objects.filter(image__isnull=False).values(
        'title', 'slug', 'image'
    )[:carousel_size]

    return {
        'categories': categories
    }


@register.inclusion_tag('tags/related_products.html')
def related_products(product: Product, products_count: int = 4) -> dict:
    """
    data for the related products
    """
    return {
        'related_products': find_related_products(product.id, products_count),
        'site': settings.SITE_DATA
    }


@register.inclusion_tag('tags/featured_products.html')
def featured_products() -> dict:
    """
    featured products block from the index page
    """
    products: QuerySet = find_related_products(None, 8)
    categories: dict = {p.category.slug: p.category.title for p in products}

    return {
        'featured_products': products,
        'categories': categories,
        'site': settings.SITE_DATA
    }
