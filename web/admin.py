from django.contrib import admin
from .models import Post, PostAdditionalImages
    # PostAdditionalText


class PostAdditionalImageAdmin(admin.StackedInline):
    model = PostAdditionalImages


# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     inlines = [PostAdditionalImageAdmin]
#
#     class Meta:
#         model = Post


@admin.register(PostAdditionalImages)
class PostImageAdmin(admin.ModelAdmin):
    pass




# class PostAdditionalTextAdmin(admin.StackedInline):
#     model = PostAdditionalText


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostAdditionalImageAdmin]

    class Meta:
        model = Post

#
# @admin.register(PostAdditionalText)
# class PostAdditionalTextAdmin(admin.ModelAdmin):
#     pass
