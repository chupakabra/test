from factory import Factory
from models import Person

class PersonFactory(Factory):
	FACTORY_FOR = Person
	
	name = "Name"
	last_name = "Last_Name"
	birth_date = "1929-03-03"
	bio = "FDGDSHFG"
	email = "example@gmail.com"
	jabber = "example@example.com"
	skype = "skype"
	other = "other"
