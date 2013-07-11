from django.test import TestCase
from django.core.urlresolvers import reverse
from http_request_storage.models import HttpRequestStorage
from django.test.utils import override_settings
from gen_info import views, urls


class RequestStorageMiddlewareTests(TestCase):

    def test_middleware_on(self):
        """Check the case when RequestStorageMiddleware is specified
        in settings"""
        response = self.client.get(reverse('http_requests:requests'))
        self.assertEqual(response.status_code, 200)
        cur_request = HttpRequestStorage.objects.get(
            path=reverse('http_requests:requests'))
        self.assertNotEqual(cur_request, None)
        response = self.client.get(reverse('gen_info:main'))
        self.assertNotEqual(HttpRequestStorage.objects.get(
                            path=reverse('gen_info:main')), None)

    @override_settings(
        MIDDLEWARE_CLASSES=(
            'django.middleware.common.CommonMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware'))
    def test_middleware_off(self):
        """Check the case when RequestStorageMiddleware is not specified
        in settings"""
        response = self.client.get(reverse('http_requests:requests'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(HttpRequestStorage.objects.all(), [])
        self.assertQuerysetEqual(response.context['first_requests'], [])


class HttpRequestStorageViewTests(TestCase):

    """def test_main_redirection(self):
        \"""Check the redirection from the main page to requests page\"""
        response = self.client.get(reverse('gen_info:main'))
        self.assertRedirects(response, reverse('http_requests:requests'))"""

    def test_requests(self):
        """Check the right opening and content of the requests page"""
        response = self.client.get(reverse('gen_info:main'))
        response = self.client.get(reverse('http_requests:requests'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, reverse('gen_info:main'))
        self.assertContains(response, reverse('http_requests:requests'))
