from django import views
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from shop_user.forms import UserSignUpForm, UserProfileForm

User = get_user_model()


class ShopUserProfile(views.generic.UpdateView):
    """
    Профиль пользователя
    """
    template_name = 'shop_user/profile.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('user-profile')

    def get_object(self, queryset=None):
        return User.objects.get(pk=self.request.user.id)


class ShopUserSignUp(views.generic.FormView):
    """
    Регистрация пользователя
    """
    template_name = 'shop_user/signup.html'
    form_class = UserSignUpForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
