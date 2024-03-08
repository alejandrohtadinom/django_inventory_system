from django.db import models
from django.db.models.fields.related import ManyToManyField


# Main item model
class Item(models.Model):
    name = models.CharField(max_length=255)
    descrition = models.TextField()
    qtty = models.IntegerField()
