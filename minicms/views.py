# encoding: utf-8
import markdown
from django import http
from django.shortcuts import render_to_response
from django.template import RequestContext

from minicms import utils


def preview(request):
    return http.HttpResponse(
        markdown.markdown(request.REQUEST.get('data', 'No content posted')),
        'text/html'
    )


def show_page(request, slug):
    lang = getattr(request, 'LANGUAGE_CODE', settings.LANGUAGE_CODE)
    page = utils.get_page(lang, slug, full=True)
    if not page:
        raise http.Http404

    return render_to_response(
        'minicms/default.html', {'page': page},
        RequestContext(request))
