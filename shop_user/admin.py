from django.contrib import admin

from shop_user.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    search_fields = 'username', 'last_name'
