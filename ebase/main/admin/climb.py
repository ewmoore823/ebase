from django.contrib import admin

from main.models import climb_models

admin.site.register(climb_models.Boulder)
admin.site.register(climb_models.SportRoute)
