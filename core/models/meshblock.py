from django.contrib.gis.db import models


class Meshblock(models.Model):
    """
    Class for NZ Census meshblocks.
    Posts will be placed within a meshblock, then data will be displayed on a chloropleth map
    """
    geo = models.PolygonField()