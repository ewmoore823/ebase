from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Climb(models.Model):
    name = models.CharField(max_length=255)
    grade = models.CharField(max_length=50)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Ascent(models.Model):
    style = models.CharField(max_length=255, choices=ASCENT_CHOICES)
