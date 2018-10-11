import secretballot
from django.contrib.gis.db import models

class Meshblock(models.Model):
    """
    Class for NZ Census meshblocks.
    Posts will be placed within a meshblock, then data will be displayed on a choropleth map
    """
    geom = models.MultiPolygonField()
    description = models.TextField(blank=True, null=True)

    @property
    def name_or_id(self):
        return str(self)

    @property
    def count_posts(self):
        return self.post_meshblock_fk.count()

    @property
    def posts_set(self):
        return self.post_meshblock_fk.all()

    @property
    def score_cell(self):
        """
        Determine the 'score' of the cell for visualisation purposes
        -1: 100% downvotes
        0:  equal score
        +1: 100% upvotes
        """
        if self.vote_total == 0:
            return 0
        return (self.total_upvotes - self.total_downvotes) /\
               (self.total_upvotes + self.total_downvotes)


    def __unicode__(self):
        if self.description is not None:
            return self.description
        return str(self.id)

    def __str__(self):
        if self.description is not None:
            return self.description
        return str(self.id)


secretballot.enable_voting_on(Meshblock)
# NB: at this stage voting only works on parent posts, modify voting methods in views.py to modify