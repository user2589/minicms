# -*- coding: utf-8 -*-
import views
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^preview',    views.preview,    name='django_markdown_preview'),
    (r'^(q?.+)/?$',     views.show_page),
)
