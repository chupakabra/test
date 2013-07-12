from django.test import TestCase
from django.core.urlresolvers import reverse


class PersonFormViewTests(TestCase):
	
     def test_form_page(self):
		response = self.client.get(reverse('form:form'))
		self.assertEqual(response.status_code, 200)
