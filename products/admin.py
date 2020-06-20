from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from .models import Product, ProductCategory, ProductImage


class ProductImageAdminInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', 'category')}
    inlines = ProductImageAdminInline,
    exclude = 'images',


@admin.register(ProductCategory)
class ProductCategoryAdmin(TreeAdmin):
    form = movenodeform_factory(ProductCategory)
    prepopulated_fields = {'slug': ('title',)}

# class ProductVariantCharacteristicInline(admin.TabularInline):
#     model = ProductVariantCharacteristic
#     extra = 1


# @admin.register(ProductVariantCharacteristic)
# class ProductVariantCharacteristic(admin.ModelAdmin):
#     list_filter = 'product_variant',


# @admin.register(ProductVariant)
# class ProductVariantAdmin(admin.ModelAdmin):
#     inlines = ProductVariantCharacteristicInline,
#     list_filter = 'parent_product',
