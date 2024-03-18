from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    category = models.ManyToManyField("Category")


class Category(models.Model):
    title = models.CharField(max_length=255)
