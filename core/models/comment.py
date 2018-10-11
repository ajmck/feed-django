from .meshblock import Meshblock
from .postAbstract import PostAbstract
from .post import Post
from django.contrib.gis.db import models
from django.db.models import CASCADE


class Comment(PostAbstract):
    class Meta:
        abstract = False
        ordering = ['pub_date']
        
    parent = models.ForeignKey(Post, on_delete=CASCADE, related_name='comments_fk')

    # Overwrite post_meshblock of abstract class due to related name conflict
    post_meshblock = models.ForeignKey(Meshblock, on_delete=CASCADE, null=True, blank=True,
                                       related_name='comment_meshblock_fk')
