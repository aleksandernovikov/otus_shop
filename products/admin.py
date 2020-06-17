from django.contrib import admin

from .models import Product, ProductVariant, ProductVariantCharacteristic


class ProductVariantCharacteristicInline(admin.TabularInline):
    model = ProductVariantCharacteristic
    extra = 1


@admin.register(ProductVariantCharacteristic)
class ProductVariantCharacteristic(admin.ModelAdmin):
    list_filter = 'product_variant',


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    inlines = ProductVariantCharacteristicInline,
    list_filter = 'parent_product',


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
