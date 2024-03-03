from django.db import models
from django.db.models.fields.related import ManyToManyField


# Main item model
class Item(models.Model):
    name = models.CharField(max_length=255)
    descrition = models.TextField()
    qtty = models.IntegerField()
    category = ManyToManyField("Category")


class Category(models.Model):
    name = models.CharField(max_length=255)


class Warehouse(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)


class location(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)