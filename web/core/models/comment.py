from .post import Post
from django.contrib.gis.db import models
from django.db.models import CASCADE


class Comment(Post):
    parent = models.ForeignKey(Post, on_delete=CASCADE, related_name='parent_post')