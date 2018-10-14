from rest_framework.generics import ListAPIView
from rest_framework_gis.filters import InBBoxFilter, DistanceToPointFilter
from core.models import Post, Comment, Meshblock
from rest_framework import viewsets
from .serializers import PostSerializer, MeshblockSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class MeshblockViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Filter by extent - inbboxfilter - ?in_bbox=a,b,c,d
    # Filter by distance - DistanceToPointFilter - ?dist=(metres)&point=(lon, lat)
    """
    queryset = Meshblock.objects.all()
    serializer_class = MeshblockSerializer
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'   # will this need to be a new point / centroid?
    filter_backends = (InBBoxFilter, DistanceToPointFilter, )
    bbox_filter_include_overlapping = True
    distance_filter_convert_meters = True  # ensures dist query search is performed in metres


'''
class PostGeoJsonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostGeoJsonSerializer
'''
