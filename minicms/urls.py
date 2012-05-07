# encoding: utf-8

from django.conf.urls import patterns

urlpatterns = patterns('',
    (r'^(\w+)/$', 'minicms.views.show_page'),
)
