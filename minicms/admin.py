# encoding: utf-8

from django.contrib import admin
from minicms.models import Page
from django import forms
from django_markdown.widgets import MarkdownWidget


class PageAdminForm(forms.ModelForm):
    content = forms.CharField(widget=MarkdownWidget())

    class Meta:
        model = Page


class PageAdmin(admin.ModelAdmin):
    form = PageAdminForm

    list_display = ('name', 'lang', 'title')
    list_filter = ('lang',)

admin.site.register(Page, PageAdmin)
