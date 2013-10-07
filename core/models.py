import os.path

from django.db import models
from sorl.thumbnail import ImageField


class Chessboard(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)


class Photo(models.Model):

    def determine_path(instance, filename):
        return os.path.join('uploads', 'chessboards', str(instance.id), filename)

    chessboard = models.ForeignKey("core.Chessboard")
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = ImageField(upload_to=determine_path)
    row = models.IntegerField()
    column = models.IntegerField()



