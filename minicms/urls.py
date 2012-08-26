# -*- coding: utf-8 -*-
import views
from django.conf.urls.defaults import url, patterns

urlpatterns = patterns('',
    url(r'^(.+)$', views.show_page, name='minicms'),
)
