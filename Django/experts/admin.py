from django.contrib import admin

from .models import Expert, Topic, News, Link

admin.site.register(Expert)
admin.site.register(Topic)
admin.site.register(News)
admin.site.register(Link)