# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.views.static import serve

from . import views

urlpatterns = [
    url(r'^/$', views.home, name='home'),
]

if settings.DEBUG:
    urlpatterns += [
        url(
            r'^media/(?P<path>.*)$',
            serve, {
                'document_root': settings.MEDIA_ROOT,
            }
        ),
    ]
    urlpatterns += staticfiles_urlpatterns()
