# encoding: utf-8

from django.conf import settings
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext

from minicms.models import Page


def show_page(request, name):
    lang = request.LANGUAGE_CODE

    page = _get_page(name, lang)
    if not page:
        raise Http404

    unique_pages = Page.objects.values_list('name', flat=True).distinct()

    menu = [_get_page(n, lang) for n in unique_pages]

    return render_to_response('minicms/default.html',
                              {'page': page, 'menu': menu},
                              RequestContext(request))


def _get_page(name, lang):
    """
    Returns more prefered (current language, default or any available) QuerySet
    of Pages (which can contain zero or one objects)
    """
    default_lang = settings.LANGUAGE_CODE
    # in most cases (menu constructing) we don't need `content`, so defer it
    pages = Page.objects.filter(name=name).defer('content')

    pages_by_lang = {}
    for page in pages:
        pages_by_lang[page.lang] = page

    page = pages_by_lang.get(lang)
    if not page and lang != default_lang:
        page = pages_by_lang.get(default_lang)

    if not page:
        try:
            page = pages[0]
        except IndexError:
            return None

    return page
