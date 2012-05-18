from django import forms
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from django.utils import simplejson


class MarkdownWidget(forms.Textarea):

    class Media:
        js = (
            'minicms/jquery.markitup.js',
            'minicms/markdown.js',
        )
        css = {
            'screen': (
                'minicms/skins/simple/style.css',
                'minicms/markdown.css',
            )
        }

    def render(self, name, value, attrs=None):
        html = super(MarkdownWidget, self).render(name, value, attrs)

        editor_settings = getattr(settings, 'MARKDOWN_EDITOR_SETTINGS', {})
        editor_settings['previewParserPath'] = reverse('minicms_markdown_preview')

        html += '<script type="text/javascript">miu.init(\'%s\', %s)</script>' % (attrs['id'], simplejson.dumps(editor_settings))

        return mark_safe(html)
