# encoding: utf-8
from django.conf import settings

from models import Page


def get_page(lang, slug, full=False):
    """
    Gets page for specified slug and language with fallback to default
    language.  Returns None if no pages found. By default (since in most cases
    this function called by menu and breadcrumbs constructors) fetches only
    subset of model's fields. This behavior can be omitted by setting `full`
    argument to `True`
    """
    slug = slug.strip('/')

    pages_for_slug = Page.objects.filter(slug=slug)
    if not full:
        pages_for_slug = pages_for_slug.only('lang', 'slug', 'name')

    page = pages_for_slug.filter(lang=lang)
    default_lang = settings.LANGUAGE_CODE
    if lang != default_lang and not page:
        page = pages_for_slug.filter(lang=default_lang)

    if page:
        return page[0]
    return None
