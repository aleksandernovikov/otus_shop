from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from products.models.cart import CartProduct
from .models.product_category import ProductCategory
from .models.product import Product
from .models.product_image import ProductImage


class ProductImageAdminInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Product
        fields = '__all__'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    prepopulated_fields = {'slug': ('title', 'category')}
    inlines = ProductImageAdminInline,
    exclude = 'images',
    autocomplete_fields = 'category',


@admin.register(ProductCategory)
class ProductCategoryAdmin(TreeAdmin):
    form = movenodeform_factory(ProductCategory)
    prepopulated_fields = {'slug': ('title',)}
    ordering = 'title',
    search_fields = 'title', 'slug'


@admin.register(CartProduct)
class CartProductAdmin(admin.ModelAdmin):
    list_filter = 'owner',
    ordering = 'owner',
