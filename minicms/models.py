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
        default=settings.LANGUAGE_CODE
    )
    slug = models.CharField(_('slug'), db_index=True, max_length=50)
    name = models.CharField(_('page name'), max_length=100)
    title = models.CharField(_('page title'), max_length=100)

    keywords = models.CharField(_('page keywords'), max_length=255, blank=True, default="")
    description = models.CharField(_('page description'), max_length=255, blank=True, default="")

    markdown = models.TextField(_('markdown content'))

    @models.permalink
    def get_absolute_url(self):
        return ('minicms.views.show_page', [self.name])

    @property
    def content(self):
        return safestring.mark_safe(markdown.markdown(self.markdown))

    _parent_slug = None
    @property
    def parent_slug(self):
        if self._parent_slug:
            return self._parent_slug
        chunks = self.slug.rsplit('/', 1)
        self._parent_slug = len(chunks)>1 and chunks[0] or None
        return self._parent_slug

    def __unicode__(self):
        return u'%s (%s) at %s' % (self.name, self.lang, self.slug)

    class Meta:
        unique_together = (('name', 'lang'),)

    def save(self, *args, **kwargs):
        if self.slug:
            self.slug = self.slug.strip('/')
        return super(Page, self).save(*args, **kwargs)
