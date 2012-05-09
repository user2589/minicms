# -*- coding: utf-8 -*-
import views
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^(q?.+)/?$',     views.show_page),
)
