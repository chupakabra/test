from django.utils import unittest

from django.test import TestCase
from gen_info.models import *

class PersonViewTests(TestCase):
	reset_sequences = True
	"""If no information about person or its contacts Error 404 should be displayed"""
	def test_main_view_no_person_info(self):
		response = self.client.get('gen_info/main.html')
		self.assertEqual(response.status_code, 404)
		self.assertEqual(response.context['person'], None)
		self.assertEqual(response.context['contacts'], None)

	"""Context checking"""
	def test_main(self):
		person = Person.objects.create(name="Name", last_name="Last_Name", birth_date="1929-03-03", bio="FDGDSHFG")
		contacts = Contacts.objects.create(person=person, email="example@com.ua", jabber="example@com.ua", skype="skype")
		response = self.client.get('gen_info/main.html')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context['person'],'<Person: Name Last_Name>','<Contacts: example@com.ua>')
		self.assertEqual(response.context['contacts'],'<Contacts: example@com.ua>')


