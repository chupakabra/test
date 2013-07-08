from django.test import TestCase
from person_factory import PersonFactory
	 
class PersonViewTests(TestCase):
	reset_sequences = True
	"""If no information about person or Error 404 should be displayed"""
	def test_main_view_no_person_info(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 404)

	"""Context checking"""
	def test_main(self):
		person = PersonFactory()
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(str(response.context['person']), 'Name Last_Name')


