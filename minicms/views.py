# encoding: utf-8

from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from minicms.models import Page


def show_page(request, name):
    lang = request.LANGUAGE_CODE

    page = get_object_or_404(_get_page(name, lang))

    unique_pages = Page.objects.values_list('name').distinct()

    # in menu, we probably don't need `content`, so defer it
    # also, note the comma - `unique_pages` is a list of tuples
    menu = [_get_page(n, lang).defer('content')[0] for n, in unique_pages]

    return render_to_response('minicms/default.html',
                              {'page': page, 'menu': menu},
                              RequestContext(request))


def _get_page(name, lang):
    """
    Returns more prefered (current language, default or any available) not
    evaluated QuerySet of Pages (which can contain zero or one objects)
    """
    default_lang = settings.LANGUAGE_CODE
    langlist = [lang]

    if default_lang != lang:
        langlist.append(default_lang)

    pages = Page.objects.filter(name=name)

    for l in langlist:
        page = pages.filter(lang=l)
        if page.exists():
            return page

    return pages[:1]
