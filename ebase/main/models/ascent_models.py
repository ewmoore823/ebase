from __future__ import unicode_literals

from django.db import models

from utils import ascent as ascent_utils


class Ascent(models.Model):
    style = models.CharField(max_length=255, choices=ascent_utils.ASCENT_STYLE_CHOICES)
    date = models.DateField()


class BoulderAscent(Ascent):
    climb = models.ForeignKey('Boulder')


class SportAscent(Ascent):
    climb = models.ForeignKey('SportRoute')
