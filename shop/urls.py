from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from products.views import CartProductView
from shop import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('shop_user.urls')),

    path('', include('usability.urls')),
    path('shop/', include('products.urls')),
    path('blog/', include('blog.urls')),

    path('api/', include('products.api.urls')),
    path('cart/', CartProductView.as_view(), name='cart'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
