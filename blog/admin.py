from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from blog.models import Post, PostCategory


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(PostCategory)
class PostCategoryAdmin(TreeAdmin):
    form = movenodeform_factory(PostCategory)
    prepopulated_fields = {'slug': ('title',)}
