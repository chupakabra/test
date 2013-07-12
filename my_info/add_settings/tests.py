from django.test import TestCase
from django.conf import settings
from django.core.urlresolvers import reverse
from django.test.utils import override_settings


class ContextProcessorSettingsTest(TestCase):

    def test_template_context_processor_on(self):
        """Check the case when context_processor.settings is specified
        in settings"""
        response = self.client.get(reverse('add_settings:settings'))
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.context['settings'], {})
        self.assertContains(response, 'STATICFILES_FINDERS')

    """@override_settings(
           TEMPLATE_CONTEXT_PROCESSORS=(
               'django.contrib.auth.context_processors.auth',
               'django.core.context_processors.debug',
               'django.core.context_processors.i18n',
               'django.core.context_processors.media',
               'django.core.context_processors.static',
               'django.core.context_processors.tz',
               'django.contrib.messages.context_processors.messages'))
     def test_template_context_processor_off(self):
        \"""Check the case when context_processor.settings is not specified
        in settings\"""
        response = self.client.get(reverse('add_settings:settings'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['settings'], {})
        self.assertNotContains(response, 'STATICFILES_FINDERS')"""
