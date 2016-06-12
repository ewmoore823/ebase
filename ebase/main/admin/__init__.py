from django.contrib import admin

from main.models import climb_models
from main.models import ascent_models

admin.site.register(climb_models.Boulder)
admin.site.register(climb_models.SportRoute)
admin.site.register(ascent_models.BoulderAscent)
admin.site.register(ascent_models.SportAscent)

# Register your models here.
