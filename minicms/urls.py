# -*- coding: utf-8 -*-
import views
from django.conf.urls.defaults import url, patterns

urlpatterns = patterns('',
    url(r'^preview', views.preview, name='django_markdown_preview'),
    (r'^(.+)/$', views.show_page),
)
