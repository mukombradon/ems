
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib.auth import views as auth_views

from .views import *


#Translated
urlpatterns = (

	path('venues/', venues, name='venues'), 
	path('add-venue/', create_venue, name='add-venue'),
	path('my-venues/', my_venues, name='my_venues'),
	path('edit_venue/<venue_id>/', edit_venue, name='edit_venue'),
	path('venue_details/<venue_id>/', venue_details, name='venue_details'),

)
