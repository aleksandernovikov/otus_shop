from django import views
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from shop_user.forms import UserSignUpForm, UserProfileForm

User = get_user_model()


class ShopUserProfile(views.generic.UpdateView):
    template_name = 'shop_user/profile.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('user-profile')

    def get_queryset(self):
        user_id = self.request.user.id
        user = User.objects.get(pk=user_id)
        return user

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ShopUserSignUp(views.generic.FormView):
    template_name = 'shop_user/signup.html'
    form_class = UserSignUpForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
