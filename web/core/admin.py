from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Post, Comment, LocationBlock
# Register your models here.


class CommentInline(admin.TabularInline):
    model = Comment
    fk_name = "parent"
    extra = 0
    readonly_fields = ["pub_date"]


class PostAdmin(admin.ModelAdmin):
    model = Post
    readonly_fields = ["pub_date"]
    inlines = [
        CommentInline,
    ]


class LocationAdmin(OSMGeoAdmin):
    # Coordinates for Dunedin
    default_lat = -45.8788
    default_lon = 170.5028

admin.site.register(Post, PostAdmin)
admin.site.register(LocationBlock, LocationAdmin)