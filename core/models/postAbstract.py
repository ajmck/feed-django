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

    NOT_REVIEWED = "NR"
    AZURE_APPROVE = "AA"
    AZURE_BLOCK = "AB"
    MANUAL_APPROVE = "MA"
    MANUAL_BLOCK = "MB"
    DOWNVOTED = "DV"

    MODERATION_CHOICES = (
        (NOT_REVIEWED, "Not Reviewed (Hidden)"),
        (AZURE_APPROVE, "Azure Approved"),
        (AZURE_BLOCK, "Azure Blocked (Hidden)"),
        (MANUAL_APPROVE, "Manually Approved"),
        (MANUAL_BLOCK, "Manually Blocked (Hidden)"),
        (DOWNVOTED, "Downvoted (Hidden)")
    )

    id = models.AutoField(primary_key=True)
    body = models.CharField(max_length=POST_BODY_LENGTH)
    pub_date = models.DateTimeField('Time Posted', default=timezone.now)
    # votes = models.IntegerField(default=0) # converted to secretballot
    post_location = models.PointField(null=True, blank=True)
    moderation = models.CharField(max_length=2,
                                  choices=MODERATION_CHOICES,
                                  default=NOT_REVIEWED,)

    post_meshblock = models.ForeignKey(Meshblock, on_delete=CASCADE, null=True, blank=True)
    # related_name='post_meshblock_fk')

    def __str__(self):
        return self.body


secretballot.enable_voting_on(PostAbstract)