from django.db.models import *

class Person(Model):
	name = CharField(max_length=20)
	surname = CharField(max_length=50)
	birth_date = DateField()
	bio = TextField()
	contacts = TextField()
	
	def __unicode__(self):
		return u'%s %s' % (self.name, self.surname)
