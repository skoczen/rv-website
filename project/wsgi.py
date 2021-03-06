# -*- coding: utf-8 -*-
"""
WSGI config for project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import locale
try:
    locale.setlocale(locale.LC_ALL, str('en_US.UTF-8'))
    locale.setlocale(locale.LANG, str('en_US.UTF-8'))
except:
    locale.setlocale(locale.LC_ALL, str('C.UTF-8'))
    # locale.setlocale(locale.LANG, str('C.UTF-8'))
import os
from sys import path

PROJECT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
BASE_DIR = os.path.join(PROJECT_DIR, "..")
APPS_DIR = os.path.join(PROJECT_DIR, "apps")
path.insert(0, BASE_DIR)
path.insert(0, PROJECT_DIR)
path.insert(0, APPS_DIR)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

application = get_wsgi_application()
