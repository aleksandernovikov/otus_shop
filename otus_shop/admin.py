from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from otus_shop.models import ProductCategory, Product, Cart, Characteristic, ProductVariantCharacteristic, Measure, \
    ProductVariant


# class ProductCharacteristicInline(admin.TabularInline):
#     model = ProductVariantCharacteristic
#     extra = 1


class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 1


@admin.register(ProductCategory)
class ProductCategoryAdmin(TreeAdmin):
    form = movenodeform_factory(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = ProductVariantInline,
    pass


@admin.register(Measure)
class MeasureAdmin(admin.ModelAdmin):
    pass


@admin.register(Characteristic)
class CharacteristicAdmin(admin.ModelAdmin):
    pass


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_filter = 'user',
