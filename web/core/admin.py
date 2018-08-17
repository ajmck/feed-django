from django.contrib import admin
from .models import Post, Comment
# Register your models here.


class CommentInline(admin.TabularInline):
    model = Comment
    fk_name = "parent"
    extra = 0


class PostAdmin(admin.ModelAdmin):
    model = Post
    inlines = [
        CommentInline,
    ]


admin.site.register(Post, PostAdmin)
