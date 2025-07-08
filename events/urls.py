
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib.auth import views as auth_views

from .views import *


#Translated
urlpatterns = (

	path('create-event/', create_event, name='create-event'),
	path('events/', events, name='events'),
	path('categories/', categories, name='categories'),
	path('event_details/<event_id>/', event_details, name='event_details'),
	path('edit_event/<event_id>/', edit_event, name='edit_event'),
	path('register/<int:event_id>/', register_event, name='register_event'),#event registration
	path('my-events/', my_events, name='my_events'),
 	path('event/<int:event_id>/attendees/', manage_attendees, name='manage_attendees'),
    path('attendee/<int:registration_id>/remove/', remove_attendee, name='remove_attendee'),
	# path('user_profile/<user_id>/', user_profile, name='user_profile'),

)
