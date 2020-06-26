from django.contrib import admin

from shop_user.models import ShopUser


@admin.register(ShopUser)
class ShopUserAdmin(admin.ModelAdmin):
    search_fields = 'username', 'last_name'
