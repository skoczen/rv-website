# -*- coding: utf-8 -*-
from django.conf import settings
from django_hosts import patterns, host

if hasattr(settings, "IS_LIVE") and settings.IS_LIVE:
    host_patterns = patterns(
        '',
        host(r'', 'project.host_urls.website', name='website'),
        host(r'root', 'project.host_urls.website', name='root'),
    )
else:
    host_patterns = patterns(
        '',
        host(r'', 'project.host_urls.root', name='root'),
        host(r'website', 'project.host_urls.website', name='website'),
    )
