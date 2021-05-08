from django.contrib import admin
from .models import *
from tinymce.widgets import TinyMCE


class PostAdditionalImageAdmin(admin.StackedInline):
    model = PostAdditionalImages


@admin.register(PostAdditionalImages)
class PostImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostAdditionalImageAdmin]

    class Meta:
        model = Post
