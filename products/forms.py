from django import forms
from django.utils.translation import gettext_lazy as _

from products.models.order import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'first_name', 'last_name',
            'state', 'city', 'street', 'building',
            'phone', 'post_code',
            'customer_notes'
        )
        widgets = {
            'street': forms.TextInput(attrs={'class': 'checkout__input__add', 'placeholder': _('Street Address')}),
            'building': forms.TextInput(attrs={'placeholder': _('Apartment, suite, unite ect (optinal)')}),
            'customer_notes': forms.TextInput(
                attrs={'placeholder': _('Notes about your order, e.g. special notes for delivery.')})
        }
