from django import views


class IndexView(views.generic.TemplateView):
    template_name = 'products/index.html'
