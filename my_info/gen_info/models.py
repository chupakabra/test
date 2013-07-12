from django.db.models import *
from PIL import Image


class Person(Model):
    name = CharField(max_length=20)
    last_name = CharField(max_length=50)
    birth_date = DateField()
    photo = ImageField(upload_to="images/", blank=True, null=True)
    bio = TextField()
    email = EmailField(max_length=75)
    jabber = EmailField(max_length=75)
    skype = CharField(max_length=50)
    other = TextField(blank=True)

    def __unicode__(self):
        return u'%s %s' % (self.name, self.last_name)
