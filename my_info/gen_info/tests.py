from django.test import TestCase
from gen_info.models import Person
	 
class PersonViewTests(TestCase):
	reset_sequences = True
	"""If no information about person or Error 404 should be displayed"""
	def test_main_view_no_person_info(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 404)

	"""Context checking"""
	def test_main(self):
		person = Person.objects.create(name = "Name", last_name = "Last_Name",\
		                               birth_date = "1929-03-03", bio = "FDGDSHFG",\
		                               email = "example@gmail.com", \
		                               jabber = "example@example.com", \
		                               skype = "skype", other = "other")
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(str(response.context['person']), 'Name Last_Name')


