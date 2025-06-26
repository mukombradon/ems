from django.contrib import admin

# Register your models here.

from .models import Venue, VenueImage

admin.site.register(Venue)
admin.site.register(VenueImage)
