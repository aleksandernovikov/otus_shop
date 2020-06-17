from django import views


class ContactsView(views.generic.TemplateView):
    template_name = 'usability/contacts.html'
