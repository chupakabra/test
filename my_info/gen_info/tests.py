from django.test import TestCase
from gen_info.models import Person
from django.core.urlresolvers import reverse


class PersonViewTests(TestCase):

    def test_main_view_no_person_info(self):
        """If no information about person or Error 404 should be displayed"""
        response = self.client.get(reverse('gen_info:main'))
        self.assertEqual(response.status_code, 404)

    def test_main(self):
        """Context checking"""
        person = Person.objects.create(
            name="Name", last_name="Last_Name",
            birth_date="1929-03-03", bio="FDGDSHFG",
            email="example@gmail.com",
            jabber="example@example.com",
            skype="skype", other="other")
        response = self.client.get(reverse('gen_info:main'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, person.last_name)
        self.assertEqual(str(response.context['person']), 'Name Last_Name')
