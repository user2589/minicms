# encoding: utf-8

from django.contrib import admin
from minicms import models
from django_markdown.admin import MarkdownModelAdmin

class PageAdmin(MarkdownModelAdmin):
    list_display = ('name', 'lang', 'title')
    list_filter = ('lang',)

admin.site.register(models.Page, PageAdmin)
