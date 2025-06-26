
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib.auth import views as auth_views

from .views import *


#Translated
urlpatterns = (

	path('create-event/', create_event, name='create-event'), 
	path('event_list/', events, name='events_list'),
	path('categories/', categories, name='categories'),


	# path('user_profile/<user_id>/', user_profile, name='user_profile'),

)
