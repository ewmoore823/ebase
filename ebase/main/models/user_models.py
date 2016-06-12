from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class MemberProfile(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    sport_ascents = models.ManyToManyField('SportAscent')
    boulder_ascents = models.ManyToManyField('BoulderAscent')

    def __str__():
        return "{0} {1}".format(first_name, last_name)
