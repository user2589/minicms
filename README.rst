minicms
#######

**minicms** is simple CMS app for Django which supports i18n in some extent and
markdown WYSIWYG editor inside admin.


Requirements
============

- django >= 1.2
- django_markdown_
- markdown


Installation
============

**minicms** should be installed using pip: ::

    pip install minicms


Setup
=====

- 'minicms', 'django_markdown' and 'django.contrib.markup' should be in your
  INSTALLED_APPS ::

    INSTALLED_APPS += (
        'minicms',
        'django_markdown',
        'django.contrib.markup',
    )

- Add 'dango_markdown' urls to base urls ::

    url('^markdown/', include('django_markdown.urls'))

- Add 'minicms' urlpattern to base urls and specify view function ::

    ('^cms/(.+)/', 'minicms.views.show_page', name='minicms')

  Of course, you may don't use any prefix at all. Just put below code at the end
  of urlpatterns: ::

    ('^(.+)/', 'minicms.views.show_page', name='minicms')

- Create template 'minicms/default.html' somewhere Django can find it

- Sync your database using ``manage.py syncdb``


Use minicms
===========

The main idea of **minicms** is that you want to have same content for each
language. I. e. page in one language must be (or desirable to be) available in
other language. If it isn't available, pages in default language will be showed
to user. If it isn't available even for default language, **minicms** will try
to show page in any other language or raise ``404 (Not Found)`` exception if
didn't find anything.

So, user will always see any of available pages even if it isn't available in
his language. Similar to how Django translation works.

Each Page object have following attributes:

- ``name`` - identifier of a Page, must be unique withing language

- ``lang`` - in what language Page is written

- ``title`` - title of a Page

- ``content`` - content of a Page in markdown format


``name`` and ``lang`` attributes must be unique together.

**minicms** use 'minicms/default.html' template, and pass to it two context
variables: ``page`` that represents current Page object and ``menu`` that a list
of all available unique pages.

Since **minicms** use markdown as markup language, within template you should
load ``markup`` template library: ::

    {% load markup %}

and pass page content through ``markdown`` template filter: ::

    {{ page.content|markdown }}


Contributing and bug tracking
=============================

Development of **minicms** happens at github:
https://github.com/neoascetic/minicms

Also, here you can leave your suggestions or bug reports.


Contributors
============

* neoascetic_ (Pavel Puchkin)


License
=======

Licensed under a `GNU lesser general public license`_.


Copyright
=========

Copyright (c) 2012 Pavel Puchkin (neoascetic@gmail.com)

.. _GNU lesser general public license: http://www.gnu.org/copyleft/lesser.html
.. _django_markdown: https://github.com/klen/django_markdown
.. _neoascetic: https://github.com/neoascetic