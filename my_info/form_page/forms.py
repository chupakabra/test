from django.forms import *
from gen_info.models import *


class PersonForm(ModelForm):
    class Meta:
        model = Person
 
