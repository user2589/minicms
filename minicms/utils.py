# encoding: utf-8
from django.conf import settings
from django import http
import models


def get_page(lang, slug):
    slug = slug.strip('/')
    try:
        return models.Page.objects.get(slug=slug, lang=lang)
    except models.Page.DoesNotExist:
        if lang != settings.LANGUAGE_CODE:
            try:
                return models.Page.objects.get(slug=slug, lang=lang)
            except models.Page.DoesNotExist:
                pass
        raise http.Http404
