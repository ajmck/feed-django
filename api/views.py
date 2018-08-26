from core.models import Post, Comment
from rest_framework import viewsets
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer