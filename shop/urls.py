from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from shop import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('django.contrib.auth.urls')),
    path('', include('shop_user.urls')),

    path('', include('usability.urls')),
    path('shop/', include('products.urls')),
    path('blog/', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
