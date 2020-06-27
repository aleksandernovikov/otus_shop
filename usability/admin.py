from django.contrib import admin

from usability.models import Subscriber, AdminMessage, FavoriteProduct


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_filter = 'active',


@admin.register(AdminMessage)
class AdminMessageAdmin(admin.ModelAdmin):
    readonly_fields = 'name', 'email', 'message', 'ip',


@admin.register(FavoriteProduct)
class FavoriteProductAdmin(admin.ModelAdmin):
    list_filter = 'user', 'product__title'
