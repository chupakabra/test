from django.test import TestCase
from gen_info.models import *

class PersonViewTests(TestCase):
	reset_sequences = True
	"""If no information about person or Error 404 should be displayed"""
	def test_main_view_no_person_info(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 404)
	
	"""If no information about person contacts Error 404 should be displayed"""
	def test_main_view_no_contacts_info(self):
		person = Person.objects.create(name="Name", last_name="Last_Name", birth_date="1929-03-03", bio="FDGDSHFG")
		response = self.client.get('/')
		self.assertEqual(response.status_code, 404)

	"""Context checking"""
	def test_main(self):
		person = Person.objects.create(name="Name", last_name="Last_Name", birth_date="1929-03-03", bio="FDGDSHFG")
		contacts = Contacts.objects.create(person=person, email="example@com.ua", jabber="example@com.ua", skype="skype")
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(str(response.context['person']), 'Name Last_Name')
		self.assertEqual(str(response.context['contacts']), 'example@com.ua')


