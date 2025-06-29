
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
	# path('user_profile/<user_id>/', user_profile, name='user_profile'),

)
