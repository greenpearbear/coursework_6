from django.conf import settings
from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=30)
    price = models.IntegerField()
    description = models.CharField(max_length=254)
    author


class Comment(models.Model):
    # TODO добавьте поля модели здесь
    pass
