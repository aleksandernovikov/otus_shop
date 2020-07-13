from django import views
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy

from products.models.order import Order
from shop_user.forms import UserSignUpForm, CustomerProfileForm

User = get_user_model()


class ShopUserProfile(LoginRequiredMixin, views.generic.UpdateView):
    """
    Профиль пользователя
    """
    template_name = 'shop_user/profile.html'
    form_class = CustomerProfileForm
    success_url = reverse_lazy('user-profile')

    def get_object(self, queryset=None):
        try:
            return User.objects.get(pk=self.request.user.id)
        except User.DoesNotExist:
            raise Http404


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


class OrderListView(LoginRequiredMixin, views.generic.ListView):
    model = Order
    template_name = 'shop_user/orders.html'
    paginate_by = 10
