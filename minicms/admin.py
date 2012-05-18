# encoding: utf-8

from django.contrib import admin
from django.db import models
from minicms.models import Page
from minicms.widgets import MarkdownWidget


class PageAdmin(admin.ModelAdmin):
    list_display = ('lang', 'slug', 'name', 'title')
    list_display_links = ('slug',)
    list_filter = ('lang',)
    search_fields = ('slug', 'name')

    formfield_overrides = {models.TextField: {'widget': MarkdownWidget}}

admin.site.register(Page, PageAdmin)
