from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from utils import climb as climb_utils


@python_2_unicode_compatible
class Climb(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, default=None)

    def __str__(self):
        return self.name


class Boulder(Climb):
    grade = models.CharField(max_length=50, choices=climb_utils.BOULDER_GRADES)


class SportRoute(Climb):
    grade = models.CharField(max_length=50, choices=climb_utils.ROUTE_GRADES)
