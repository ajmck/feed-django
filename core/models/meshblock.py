import secretballot
from django.contrib.gis.db import models


class Meshblock(models.Model):
    """
    Class for NZ Census meshblocks.
    Posts will be placed within a meshblock, then data will be displayed on a choropleth map
    """
    geom = models.MultiPolygonField()
    name = models.TextField(blank=True, null=True)


    def __unicode__(self):
        if self.name is not None:
            return self.name
        return str(self.id)

    def __str__(self):
        if self.name is not None:
            return self.name
        return str(self.id)


secretballot.enable_voting_on(Meshblock)
# NB: at this stage voting only works on parent posts, modify voting methods in views.py to modify