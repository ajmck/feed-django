from .postAbstract import PostAbstract


class Post(PostAbstract):
    class Meta:
        abstract = False
        ordering = ['-pub_date']

