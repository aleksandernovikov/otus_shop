from django.conf import settings

from usability.models import FavoriteProduct


def site_data(request):
    if hasattr(settings, 'SITE_DATA'):
        data = settings.SITE_DATA
    else:
        data = {}
    return {
        'site': data
    }


def favorites(request):
    favorites_count = FavoriteProduct.objects.filter(user=request.user).count() if request.user.is_authenticated else 0
    return {
        'favorites_count': favorites_count
    }
