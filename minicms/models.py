# encoding: utf-8
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Page(models.Model):
    name = models.CharField(_('name'), max_length=100)
    lang = models.CharField(
        _('language'),
        max_length=10,
        choices=settings.LANGUAGES
    )
    title = models.CharField(_('title'), max_length=100)
    content = models.TextField(_('content'))

    @models.permalink
    def get_absolute_url(self):
        return ('minicms.views.show_page', [self.name])

    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.lang)

    class Meta:
        ordering = ('name',)
        verbose_name = _('page')
        verbose_name_plural = _('pages')
        unique_together = (('name', 'lang'),)
