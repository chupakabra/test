from django.core.urlresolvers import reverse
from django.test import TestCase
from gen_info.models import *

class PersonViewTests(TestCase):
	
	"""If no information about person or its contacts Error 404 should be displayed"""
	def test_main_view_no_person_info(self):
		response = self.client.get(reverse('main'))
		self.assertEqual(response.status_code, 404)
		self.assertQuerysetEqual(response.context['person'], [])
		self.assertQuerysetEqual(response.context['contacts'], [])
	
	"""Context checking"""
	def test_main_view_person_context_without_contacts(self):
		person = Person.objects.create(name="Name", last_name="Last_Name")
		contacts = Person.contacts_set.create(e_mail="example@com.ua")
		response = self.client.get(reverse('main'))
		self.assertEqual(response.status_code, 200)
		self.assertQuerysetEqual(
            response.context['person'],
            ['<Person: Name Last_Name>']
        )
		self.assertQuerysetEqual(
            response.context['contacts'],
            ['<Contacts: example@com.ua>']
        )


