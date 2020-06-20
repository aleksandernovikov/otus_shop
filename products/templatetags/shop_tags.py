from django import template

from ..models import ProductCategory

register = template.Library()


@register.inclusion_tag('tags/shop_categories.html')
def shop_categories(place):
    params = {'show_in_top': True} if place == 'top' else {'show_in_sidebar': True}
    categories = ProductCategory.objects.filter(**params)

    return {
        'categories': categories
    }
