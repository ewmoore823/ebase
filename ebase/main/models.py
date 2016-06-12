from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from utils import climb as climb_utils
from utils import ascent as ascent_utils


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


class Ascent(models.Model):
    style = models.CharField(max_length=255, choices=ascent_utils.ASCENT_STYLE_CHOICES)
    date = models.DateField()


class BoulderAscent(Ascent):
    climb = models.ForeignKey('Boulder')


class SportAscent(Ascent):
    climb = models.ForeignKey('SportRoute')
