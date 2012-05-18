# -*- coding: utf-8 -*-
import views
from django.conf.urls.defaults import url, patterns

urlpatterns = patterns('',
    url(r'^preview', views.preview, name='minicms_markdown_preview'),
    url(r'^(.+)$', views.show_page, name='minicms'),
)
