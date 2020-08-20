from django.db import models

# Create your models here.
class Release(models.Model):
    artist = models.CharField(max_length=64)
    title = models.CharField(max_length=128)
    year = models.PositiveIntegerField