from django.contrib.gis.db import models
from django.db.models import CASCADE
from django.utils import timezone
from feed.settings import POST_BODY_LENGTH
from .post import Post

# Create your models here.


class Comment(models.Model):
    body = models.CharField(max_length=POST_BODY_LENGTH)
    pub_date = models.DateTimeField('Time Posted', default=timezone.now)
    votes = models.IntegerField(default=0)
    parent = models.ForeignKey(Post, on_delete=CASCADE)
    # post_location = models.PointField(null=True, blank=True)

    def __str__(self):
        return self.body
