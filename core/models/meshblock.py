import secretballot
from django.contrib.gis.db import models


class Meshblock(models.Model):
    """
    Class for NZ Census meshblocks.
    Posts will be placed within a meshblock, then data will be displayed on a choropleth map
    """
    geom = models.MultiPolygonField()
    name = models.TextField(blank=True, null=True)


secretballot.enable_voting_on(Meshblock)