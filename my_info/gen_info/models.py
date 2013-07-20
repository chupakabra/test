from django.db.models import *
from settings import MEDIA_URL
from django.contrib import admin


class Person(Model):
    name = CharField(max_length=20)
    last_name = CharField(max_length=50)
    birth_date = DateField()
    photo = ImageField(upload_to="images", blank=True, null=True)
    bio = TextField()
    email = EmailField(max_length=75)
    jabber = EmailField(max_length=75)
    skype = CharField(max_length=50)
    other = TextField(blank=True)
    
    def photo_image(self):
        return (MEDIA_URL + self.photo.name) if self.photo else None
        
    def image_(self):
        return '<a href="/static/{0}"><img src="/static/{0}"></a>'.format(self.thumbnail)
	
	image_.allow_tags = True
    
    def __unicode__(self):
        return u'%s %s' % (self.name, self.last_name)

        
class AdminName(admin.ModelAdmin):
    list_display = ('image_',)        
