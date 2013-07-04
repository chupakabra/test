"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from gen_info import *
from gen_info,models import Person

class PersonViewTests(TestCase):
	
	"""If no information about person Error 404 should be displayed"""
	def test_main_view_no_info(self):
		response = self.client.get(reverse('main'))
		self.assertEqual(response.status_code, 404)
		self.assertQuerysetEqual(response.context['person'], [])
	
	"""Checking context of 'person' at all"""
	def test_main_view_person_context(self):
		json_text = "[{\"pk\": 1, \"model\": \"gen_info.person\", \"fields\":{\"name\": \"Name\", \"surname\": \"Surname\", \"Birth date\": \"dd.mm.yyyy\", \"bio\": {\"Birth place\": \"Some place\", \"Education\": \"Some education\", \"Work experience\": \"Some experience\"}, \"contacts\": {\"E-mail\": \"someone@gmail.com\",\"Telephone\": \"+38(098)xxxxxxx\"}}}]"
		response = self.client.get(reverse('main'))
		self.assertEqual(response.status_code, 200)
		self.assertQuerysetEqual(
            response.context['person'],
            ['<Person: Name Surname>'],
        self.assertQuerysetEqual(
            response.context['bio_dict'],
            ['<Person: {Birth place: Some place, Education: Some education, Work experience: Some experience}'],
        )
        self.assertQuerysetEqual(
            response.context['contacts_dict'],
            ['<Person: {E-mail: someone@gmail.com, Telephone: +38(098)xxxxxxx}'],
        )

