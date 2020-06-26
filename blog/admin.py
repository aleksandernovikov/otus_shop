from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from blog.models import Post, PostCategory


class PostAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = '__all__'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    prepopulated_fields = {'slug': ('title',)}
    autocomplete_fields = 'author',
    radio_fields = {"category": admin.HORIZONTAL}
    fields = (
        'author', 'category',
        ('title', 'slug'),
        'image', 'text'
    )


@admin.register(PostCategory)
class PostCategoryAdmin(TreeAdmin):
    form = movenodeform_factory(PostCategory)
    prepopulated_fields = {'slug': ('title',)}
    ordering = 'title',
    search_fields = 'title', 'slug'
