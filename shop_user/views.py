from django import views


class ShopUserProfile(views.generic.TemplateView):
    template_name = 'shop_user/profile.html'
