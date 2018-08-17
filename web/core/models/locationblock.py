from django.contrib.gis.db import models


class LocationBlock(models.Model):
    name = models.CharField(max_length=40)
    polygon = models.PolygonField()

    def __str__(self):
        return self.name