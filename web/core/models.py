from django.contrib.gis.db import models
from django.utils import timezone
from feed.settings import POST_BODY_LENGTH
# Create your models here.


class Post(models.Model):
    body = models.CharField(max_length=POST_BODY_LENGTH)
    pub_date = models.DateTimeField('Time Posted', default=timezone.now)
    # post_location = models.PointField(null=True, blank=True)

    def __str__(self):
        return self.body
