from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    priority = models.PositiveSmallIntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.name
