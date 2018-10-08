from django.contrib.gis.db import models
from django.db.models import CASCADE
from django.utils import timezone

from .meshblock import Meshblock
from feed.settings.base import POST_BODY_LENGTH
import secretballot
# Create your models here.

"""
Because comments inherited from Post were showing up in the main feed,
this is now an abstract class
"""

class PostAbstract(models.Model):
    class Meta:
        abstract = True

    id = models.AutoField(primary_key=True)
    body = models.CharField(max_length=POST_BODY_LENGTH)
    pub_date = models.DateTimeField('Time Posted', default=timezone.now)
    post_location = models.PointField(null=True, blank=True)

    post_meshblock = models.ForeignKey(Meshblock, on_delete=CASCADE, null=True, blank=True)
    # related_name='post_meshblock_fk')

    def __str__(self):
        return self.body


# Enable upvotes and downvotes
secretballot.enable_voting_on(PostAbstract)