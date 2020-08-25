from django.db import models
from django.contrib.auth.models import User

class FavRecord(models.Model):
    recordId = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.recordId)

