# encoding: utf-8

from django.contrib import admin
from minicms import models
from django_markdown.admin import MarkdownModelAdmin


class PageAdmin(MarkdownModelAdmin):
    list_display = ('lang', 'slug', 'name', 'title')
    list_display_links = ('slug',)
    list_filter = ('lang',)
    search_fields = ('slug', 'name')

admin.site.register(models.Page, PageAdmin)
