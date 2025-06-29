from django.contrib import admin

# Register your models here.
from .models import Event, EventImage

admin.site.register(Event)
admin.site.register(EventImage)