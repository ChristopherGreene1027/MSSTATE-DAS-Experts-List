from django.contrib import admin

from .models import Expert, Topic, News

admin.site.register(Expert)
admin.site.register(Topic)
admin.site.register(News)