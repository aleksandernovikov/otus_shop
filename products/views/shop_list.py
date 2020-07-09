from django import views
from django.http import Http404

from products.models.product import Product
from products.models.product_category import ProductCategory


class ShopListView(views.generic.ListView):
    """
    Browse Products
    """
    model = Product
    template_name = 'usability/pages/shop.html'
    paginate_by = 6
    allowed_sort_params = ('price', '-price')
    _category = None

    def get_queryset(self):
        """
        Sorting on shop pages
        if a category is specified, the class property is populated
        """
        queryset = self.model.objects.all()

        # optional parameters
        category_slug = self.kwargs.get('slug')
        sort_param = self.request.GET.get('sort')

        if category_slug is not None:
            try:
                self._category = ProductCategory.objects.get(slug=category_slug)
                queryset = queryset.filter(
                    category__slug=category_slug
                )
            except ProductCategory.DoesNotExist:
                raise Http404(_('Category not found'))

        if sort_param in self.allowed_sort_params:
            queryset = queryset.order_by(
                sort_param
            )

        return queryset.prefetch_related(
            'product_images'
        )

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        sort_param = self.request.GET.get('sort')

        if sort_param in self.allowed_sort_params:
            ctx['current_sorting'] = sort_param

        if self._category is not None:
            ctx['category'] = self._category
        return ctx
