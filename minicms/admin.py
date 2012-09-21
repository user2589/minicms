# encoding: utf-8

from django.contrib import admin
from django.db import models
from minicms.models import Page
from pagedown.widgets import AdminPagedownWidget

from sortable.admin import SortableAdmin


class PageAdmin(SortableAdmin):
    list_display = ('lang', 'slug', 'name', 'title',)
    list_display_links = ('slug', 'name', 'title',)
    list_filter = ('lang',)
    search_fields = ('slug', 'name',)

admin.site.register(Page, PageAdmin)
