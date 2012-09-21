# encoding: utf-8

from django.contrib import admin
from minicms.models import Page

from sortable.admin import SortableAdmin


class PageAdmin(SortableAdmin):
    list_display = ('slug', 'name', 'lang',)
    list_display_links = ('slug', 'name',)
    list_filter = ('lang',)
    search_fields = ('slug', 'name',)

admin.site.register(Page, PageAdmin)
