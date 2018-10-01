from django.contrib import admin
from django.contrib.gis.db import models
from django.contrib.gis.admin import OSMGeoAdmin

# unsure if below line works right, may need to be admin widget
from django.contrib.gis.forms.widgets import OSMWidget
from .models import Post, Comment
# Register your models here.


class CommentInline(admin.TabularInline):
    model = Comment
    fk_name = "parent"
    extra = 0
    readonly_fields = ["pub_date"]
    formfield_overrides = {models.PointField: {'widget': OSMWidget}}




class PostAdmin(admin.ModelAdmin):
    model = Post
    readonly_fields = ["pub_date"]
    inlines = [
        CommentInline,
    ]
    formfield_overrides = {models.PointField: {'widget': OSMWidget}}


class LocationAdmin(OSMGeoAdmin):
    # Coordinates for Dunedin
    default_lat = -45.8788
    default_lon = 170.5028
    formfield_overrides = {models.PointField: {'widget': OSMWidget}}


admin.site.register(Post, PostAdmin)
