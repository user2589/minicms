Minicms
#######

**Minicms** is simple CMS app for Django which supports i18n in some extent and
markdown WYSIWYG editor inside admin.

Requirements
============

- django >= 1.3
- markdown

Installation
============

**Minicms** should be installed using pip: ::

    pip install minicms

Setup
=====

- 'Minicms' should be in your INSTALLED_APPS ::

    INSTALLED_APPS += ('minicms',)

- Add 'minicms' urlpattern to base urls and specify view function ::

    ('^cms/', include('minicms.urls'))

- Make sure you have 'django.middleware.locale.LocaleMiddleware' in your
  MIDDLEWARE_CLASSES

- Sync DB ``manage.py syncdb``

Use minicms
===========

The main idea of **minicms** is that you want to have same content for each
language. I. e. page in one language must be (or desirable to be) available in
other language. If it isn't available, pages in default language will be showed
to user. If it isn't available even for default language, **minicms** raise
``404 (Not Found)``.

Each Page model have following attributes:

- ``lang`` - in what language Page is written

- ``slug`` - in fact, not slug, but Page URL. Using this, you can construct
  hierarchies of pages. For example, page with ``slug == 'pony_farm'`` is a
  child of page with ``slug == 'my/pony_farm'`` and so on

- ``name`` - page name

- ``title`` - title of a Page, more detailed than name. Mainly for using in
  ``title`` tag

- ``keywords`` - keywords associated with page, mainly for using in meta tag

- ``description`` - short description of page, mainly for using in meta tag

- ``markdown`` - raw page content in markdown format (there also ``content``
  property, which returns the content in html)

``slug`` and ``lang`` attributes must be unique together, i. e. for each
language we have only Page with some slug

**Minicms** use 'minicms/default.html' template, and pass to it current Page
object by ``page`` context variable.

There also ``minicms_breadcrumbs`` and ``minicms_menu`` template tags available
in ``minicms_tags`` tag library. See example templates_ for details.

Contributing and bug tracking
=============================

Development of **minicms** happens at github:
https://github.com/neoascetic/minicms

Also, here you can leave your suggestions or bug reports.

Contributors
============

* neoascetic_ (Pavel Puchkin)

* user2589_

License
=======

Licensed under a `GNU lesser general public license`_.

Copyright
=========

Copyright (c) 2012 Pavel Puchkin (neoascetic@gmail.com)

Markitup_: (c) 2008 Jay Salvat (http://markitup.jaysalvat.com/)

.. _Markitup:     http://markitup.jaysalvat.com/
.. _GNU lesser general public license: http://www.gnu.org/copyleft/lesser.html
.. _templates: https://github.com/neoascetic/minicms/tree/master/minicms/templates
.. _neoascetic: https://github.com/neoascetic
.. _user2589: https://github.com/user2589
