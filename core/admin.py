from django.contrib import admin
from django.contrib.gis.admin import GeoModelAdmin
from django.contrib.gis.db import models
from django.contrib.gis.admin import OSMGeoAdmin

# unsure if below line works right, may need to be admin widget
from django.contrib.gis.forms.widgets import OSMWidget

from core.models import Meshblock
from .models import Post, Comment
# Register your models here.


# class PostMeshblockInline(admin.StackedInline):
#     model = Meshblock
#     fk_name = "post_meshblock"


class CommentInline(admin.TabularInline):
    model = Comment
    fk_name = "parent"
    extra = 0
    readonly_fields = ["pub_date", "post_meshblock"]
    raw_id_fields = ["post_meshblock"]
    formfield_overrides = {models.PointField: {'widget': OSMWidget}}


class PostAdmin(admin.ModelAdmin):
    model = Post
    readonly_fields = ["pub_date", "post_meshblock"]
    inlines = [
        CommentInline,
        # PostMeshblockInline,
    ]
    raw_id_fields = ["post_meshblock"]
    formfield_overrides = {
        models.PointField: {'widget': OSMWidget},
        #   models.MultiPolygonField: {'widget': OSMWidget}
    }


class MeshblockAdmin(OSMGeoAdmin):
    model = Meshblock
    # below line fails due to being multipolygon (or something)
    # readonly_fields = ["geo"]
    modifiable = False
    # formfield_overrides = {models.MultiPolygonField: {'widget': OSMWidget}}


admin.site.register(Post, PostAdmin)
admin.site.register(Meshblock, MeshblockAdmin)
