from django.contrib import admin
from django.contrib.gis.admin import GeoModelAdmin
from django.contrib.gis.db import models
from django.contrib.gis.admin import OSMGeoAdmin

# unsure if below line works right, may need to be admin widget
from django.contrib.gis.forms.widgets import OSMWidget

from core.models import Meshblock
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


class MeshblockAdmin(OSMGeoAdmin):
    model = Meshblock
    # below line fails due to being multipolygon (or something)
    # readonly_fields = ["geo"]
    modifiable = False
    # formfield_overrides = {models.MultiPolygonField: {'widget': OSMWidget}}


admin.site.register(Post, PostAdmin)
admin.site.register(Meshblock, MeshblockAdmin)
