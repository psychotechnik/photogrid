import os.path
from django.template.defaultfilters import slugify

from django.db import models
from sorl.thumbnail import ImageField


class Chessboard(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)


class Photo(models.Model):

    def determine_path(instance, filename):
        return os.path.join('uploads', 'chessboards', slugify(instance.title), filename)

    chessboard = models.ForeignKey("core.Chessboard", related_name="photos")
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = ImageField(upload_to=determine_path)
    row = models.IntegerField()
    column = models.IntegerField()

    def __unicode__(self):
        return "%s [row %s, col %s]" % (self.title, self.row, self.column)



