from django.contrib.gis.db import models


class Landmark(models.Model):

    USER = 'US'        # This landmark has been entered by a user
    APPROVED = 'AP'    # This landmark has been approved and will show on the dropdown
    FLAGGED = 'FL'     # Content moderator has flagged this name and should not be displayed

    MODERATION_CHOICES = (
        (USER, 'User Submitted'),
        (APPROVED, 'Approved'),
        (FLAGGED, 'Flagged'),
    )

    name = models.CharField(max_length=50)
    position = models.PointField()
    moderation = models.CharField(max_length=2,
                                  choices=MODERATION_CHOICES,
                                  default=USER)


    def __str__(self):
        return self.name