# -*- coding: utf-8 -*-
from django import template
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
        pages.append(page)
        slug = page.parent_slug

    pages.reverse()

    return {'breadcrumbs': pages, 'current_page': context['page']}


@register.inclusion_tag('minicms/tags/menu.html', takes_context=True)
def minicms_menu(context):
    lang = context['LANGUAGE_CODE']
    current_page = context['page']

    pages = models.Page.objects.filter(lang=lang).only('name', 'slug')

    def get_children(parent_slug):
        children = filter(lambda p: p.parent_slug == parent_slug, pages)
        for p in children:
            p.active = (p.slug == current_page.slug)
            p.children = get_children(p.slug)
        return children

    return {'menu': get_children(None), 'current_page': context['page']}
