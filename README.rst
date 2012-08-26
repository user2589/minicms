Minicms
#######

**Minicms** is simple CMS app for Django which supports i18n in some extent and
markdown WYSIWYG editor inside admin.

Requirements
============

- django >= 1.3
- django-sortable >= 0.2.0
- django-pagedown >= 0.0.2
- markdown

Installation
============

**Minicms** should be installed using pip: ::

    pip install minicms

Setup
=====

- 'minicms', 'sortable' and 'pagedown' should be in your INSTALLED_APPS ::

    INSTALLED_APPS += ('minicms', 'sortable', 'pagedown',)

- Sync DB ``manage.py syncdb``

Use minicms
===========

Same page in different languages accessed via the same URL. If page doesn't
exist in requested locale default language is used.

**Minicms** uses 'minicms/default.html' template, passing current page in
``page`` context variable.

Page attributes you can use in template:

- ``lang`` - page language. Usually same as LANGUAGE_CODE context variable (see
  above)

- ``slug`` - page slug. All translations of the same page should have the same
  slug.  You can organize pages into some kind of hierarchy with slashes, eg: ::

    installation
        installation/requirements
        installation/steps
            installation/steps/1
            installation/steps/2
            installation/steps/3
    pricing
        pricing/free-plan

- ``name`` - localized page name. It will appear as a text under link in menu
  and breadcrumbs

- ``title`` - title of a page, intended for use in HTML title

- ``keywords`` - page keywords intended for use in HTML meta keywords (for SEO)

- ``description`` - same ask keywords but description

- ``content`` - HTML content of the page

There are also ``minicms_breadcrumbs`` and ``minicms_menu`` template tags
available in ``minicms_tags`` tag library. You can override their appearance in
templates ``minicms/tags/menu`` and  ``minicms/tags/breadcrumbs``. See example
templates_ for details.

License
=======

Distrubuted under `GNU lesser general public license`_.

Copyright
=========

Copyright (c) 2012 Pavel Puchkin (neoascetic@gmail.com)

.. _GNU lesser general public license: http://www.gnu.org/copyleft/lesser.html
.. _templates: https://github.com/neoascetic/minicms/tree/master/minicms/templates
.. _neoascetic: https://github.com/neoascetic
