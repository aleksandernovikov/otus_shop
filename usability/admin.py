from django.contrib import admin

from usability.models import Subscriber, AdminMessage


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_filter = 'active',


@admin.register(AdminMessage)
class AdminMessageAdmin(admin.ModelAdmin):
    readonly_fields = 'name', 'email', 'message', 'ip',
