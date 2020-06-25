from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class UserSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email",)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('avatar', 'username', 'first_name', 'middle_name', 'last_name', 'short_description')
        widgets = {
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'short_description': forms.TextInput(attrs={'class': 'form-control'}),
        }
