# encoding: utf-8
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import safestring

import markdown


class Page(models.Model):
    lang = models.CharField(
        _('language'),
        max_length=10,
        choices=settings.LANGUAGES,
        default=settings.LANGUAGE_CODE)

    slug = models.CharField(
        _('slug'), db_index=True, max_length=50,
        help_text=_('Page URL. First and last slashes will be stripped!'))

    name = models.CharField(_('name'), max_length=50)

    title = models.CharField(
        _('title'), max_length=100, blank=True, default="",
        help_text=_('More detailed than name, for using in `title` tag'))

    keywords = models.CharField(
        _('keywords'), max_length=255, blank=True, default="",
        help_text=_('For using in `meta` tag'))

    description = models.CharField(
        _('description'), max_length=255, blank=True, default="",
        help_text=_('For using in `meta` tag'))

    markdown = models.TextField(_('markdown content'))

    def __unicode__(self):
        return u'%s (%s) at %s' % (self.name, self.lang, self.slug)

    def get_title(self):
        return self.title or self.name

    @models.permalink
    def get_absolute_url(self):
        return ('minicms', [self.name])

    @property
    def content(self):
        return safestring.mark_safe(markdown.markdown(self.markdown))

    _parent_slug = None

    @property
    def parent_slug(self):
        if self._parent_slug:
            return self._parent_slug
        chunks = self.slug.rsplit('/', 1)
        self._parent_slug = len(chunks) > 1 and chunks[0] or None
        return self._parent_slug

    def save(self, *args, **kwargs):
        if self.slug:
            self.slug = self.slug.strip('/')
        return super(Page, self).save(*args, **kwargs)

    class Meta:
        unique_together = ('slug', 'lang'),
