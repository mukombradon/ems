
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib.auth import views as auth_views

from .views import *


#Translated
urlpatterns = (

	path('login_user/', login_user, name='login_user'), 

	path('logout/', logout, name='logout'), 

	path('register_user/', register_user, name='register_user'), 

	path('events/', events_view, name='events'), 


	# path('add_user/', add_user, name='add_user'),


	# path('user_profile/<user_id>/', user_profile, name='user_profile'),

)
