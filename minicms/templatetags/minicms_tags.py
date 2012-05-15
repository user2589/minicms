# -*- coding: utf-8 -*-
from django.conf import settings
from django import template, http

from minicms import utils, models

register = template.Library()


@register.inclusion_tag('minicms/tags/breadcrumbs.html', takes_context=True)
def minicms_breadcrumbs(context):
    lang = context['LANGUAGE_CODE']
    pages = []
    slug = context['page'].parent_slug
    while slug:
        page = utils.get_page(lang, slug)
        if not page:  # skip breadcrumbs if missing one of parents
            pages = []
            break
        pages.insert(0, page)
        slug = page.parent_slug

    return {'breadcrumbs': pages, 'current_page': context['page']}


@register.inclusion_tag('minicms/tags/menu.html', takes_context=True)
def minicms_menu(context):
    lang = context['LANGUAGE_CODE']
    current_page = context['page']

    pages = models.Page.objects.filter(lang=lang).defer('markdown')

    def get_children(parent_slug):
        children = filter(lambda x: x.parent_slug == parent_slug, pages)
        print parent_slug, children
        for p in children:
            p.active = (p.slug == current_page.slug)
            p.children = get_children(p.slug)
        return children

    return {'menu': get_children(None), 'current_page': context['page']}
