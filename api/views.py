from core.models import Post, Comment, Meshblock
from rest_framework import viewsets
from .serializers import PostSerializer, MeshblockSerializer, PostGeoJsonSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class MeshblockViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Meshblock.objects.all()
    serializer_class = MeshblockSerializer


class PostGeoJsonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostGeoJsonSerializer