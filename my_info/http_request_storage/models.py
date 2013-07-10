from django.db.models import *

class HttpRequestStorage(Model):
	date = DateTimeField()
	path_info = CharField(max_length=100)
	
	def __unicode__(self):
		return u'%s %s' % (self.date, self.path_info)
