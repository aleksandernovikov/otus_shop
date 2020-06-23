from django.conf import settings


def site_data(request):
    if hasattr(settings, 'SITE_DATA'):
        data = settings.SITE_DATA
    else:
        data = {}
    return {
        'site': data
    }
