from django.db import models


class Warehouse(models.Model):
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255)


class Location(models.Model):
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
