

from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.i18n import i18n_patterns
from django.views.static import serve
from django.views.generic.base import TemplateView
from ems.settings import DEBUG, MEDIA_ROOT

from users.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
]


urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    path('', index, name='index'),

    path('users/', include('users.urls')),

    path('venues/', include('venues.urls')), 

    path('events/', include('events.urls')), 

]

if not DEBUG:
    from ems.settings import STATIC_ROOT
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT})
    ]
