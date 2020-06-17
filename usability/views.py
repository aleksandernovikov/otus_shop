from django import views


class ContactsView(views.generic.TemplateView):
    template_name = 'usability/contacts.html'


class IndexView(views.generic.TemplateView):
    template_name = 'usability/index.html'
