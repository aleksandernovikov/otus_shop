from django import views

from ..models.product import Product


class ProductDetailsView(views.generic.DetailView):
    """
    Страница товара
    """
    model = Product
    template_name = 'usability/pages/product_details.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.prefetch_related(
            'product_images',
            'product_characteristics'
        )

    def get_context_data(self, *args, **kwargs):
        """
        Пробросим данные о фотографиях товара, чтобы не делать запрос в шаблоне
        """
        ctx = super().get_context_data(**kwargs)

        ctx.update({
            'product_images': self.object.product_images.all(),
            'product_characteristics': self.object.product_characteristics.all()
        })
        return ctx
