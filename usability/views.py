from django import views

from .models import FavoriteProduct


class FavoriteProductView(views.generic.ListView):
    model = FavoriteProduct
    template_name = 'usability/pages/favorites.html'
    paginate_by = 10
