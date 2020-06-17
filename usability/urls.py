from django.urls import path

from usability.views import ContactsView

urlpatterns = [
    path('contacts/', ContactsView.as_view(), name='contacts')
]
