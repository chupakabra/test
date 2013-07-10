from django.test import TestCase
from django.core.urlresolvers import reverse
from http_request_storage.models import HttpRequestStorage
from django.test.utils import override_settings
from django.core.urlresolvers import reverse


class RequestStorageMiddlewareTests(TestCase):
	
    def test_middleware_on(self):
        """Check the case when RequestStorageMiddleware is specified in settings"""
        response = self.client.get(reverse('http_requests:requests'))
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(HttpRequestStorage.objects.all(), [])
        self.assertNotEqual(response.context['first_requests'], [])
        
    @override_settings(MIDDLEWARE_CLASSES = (
                       'django.middleware.common.CommonMiddleware',
                       'django.contrib.sessions.middleware.SessionMiddleware',
                       'django.middleware.csrf.CsrfViewMiddleware',
                       'django.contrib.auth.middleware.AuthenticationMiddleware',
                       'django.contrib.messages.middleware.MessageMiddleware'))
    def test_middleware_off(self):
        """Check the case when RequestStorageMiddleware is not specified in settings"""
        response = self.client.get(reverse('http_requests:requests'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(HttpRequestStorage.objects.all(), [])
        self.assertEqual(response.context['first_requests'], [])
