from django.contrib import admin

from main.models import user_models

admin.site.register(user_models.MemberProfile)

