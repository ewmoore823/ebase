from django.contrib import admin

from main.models import ascent_models
admin.site.register(ascent_models.BoulderAscent)
admin.site.register(ascent_models.SportAscent)
