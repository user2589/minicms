# encoding: utf-8
from django.conf import settings
from django import http
from django.shortcuts import render_to_response
from django.template import RequestContext

from minicms import models, utils

import markdown


def preview(request):
    return http.HttpResponse(
        markdown.markdown(request.REQUEST.get('data', 'No content posted')),
        'text/html'
    )


def show_page(request, slug):

    return render_to_response('minicms/default.html',
                              {'page': utils.get_page(request.LANGUAGE_CODE, slug)},
                              RequestContext(request))
