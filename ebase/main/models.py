from __future__ import unicode_literals

ASCENT_STYLE_CHOICES = (
    ('RP', 'Redpoint'),
    ('F', 'Flash'),
    ('OS', 'Onsight'),
)

BOULDER_GRADES = (
    ('V0', 'V0'),
    ('V1', 'V1'),
    ('V2', 'V2'),
    ('V3', 'V3'),
    ('V4', 'V4'),
    ('V5', 'V5'),
    ('V6', 'V6'),
    ('V7', 'V7'),
    ('V8', 'V8'),
    ('V9', 'V9'),
    ('V10', 'V10'),
    ('V11', 'V11'),
    ('V12', 'V12'),
    ('V13', 'V13'),
    ('V14', 'V14'),
    ('V15', 'V15'),
    ('V16', 'V16')
)

ROUTE_GRADES = (
    ('5.8', '5.9'),
    ('5.9', '5.8'),
    ('5.10a', '5.10a'),
    ('5.10b', '5.10b'),
    ('5.10c', '5.10c'),
    ('5.10d', '5.10d'),
    ('5.11a', '5.11a'),
    ('5.11b', '5.11b'),
    ('5.11c', '5.11c'),
    ('5.11d', '5.11d'),
    ('5.12a', '5.12a'),
    ('5.12b', '5.12b'),
    ('5.12c', '5.12c'),
    ('5.12d', '5.12d'),
    ('5.13a', '5.13a'),
    ('5.13a', '5.13b'),
    ('5.13a', '5.13c'),
    ('5.13a', '5.13d'),
    ('5.14a', '5.14a'),
    ('5.14b', '5.14b'),
    ('5.14c', '5.14c'),
    ('5.14d', '5.14d'),
    ('5.15a', '5.15a'),
    ('5.15b', '5.15b'),
    ('5.15c', '5.15c'),
)

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
@python_2_unicode_compatible
class Climb(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, default=None)

    def __str__(self):
        return self.name


class Boulder(Climb):
    grade = models.CharField(max_length=50, choices=BOULDER_GRADES)


class SportRoute(Climb):
    grade = models.CharField(max_length=50, choices=ROUTE_GRADES)


class Ascent(models.Model):
    style = models.CharField(max_length=255, choices=ASCENT_STYLE_CHOICES)
    date = models.DateField()


class BoulderAscent(Ascent):
    climb = models.ForeignKey('Boulder')


class SportAscent(Ascent):
    climb = models.ForeignKey('SportRoute')
