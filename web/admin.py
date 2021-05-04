from django.contrib import admin
from .models import Post, PostImages


class PostImageAdmin(admin.StackedInline):
    model = PostImages


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model = Post


@admin.register(PostImages)
class PostImageAdmin(admin.ModelAdmin):
    pass
