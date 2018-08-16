from django.contrib.gis.db import models
from django.utils import timezone
from feed.settings import POST_BODY_LENGTH
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
    # votes = models.IntegerField(default=0) # converted to secretballot
    post_location = models.PointField(null=True, blank=True)


    def __str__(self):
        return self.body


secretballot.enable_voting_on(PostAbstract)