from gen_info.models import Person
from django.shortcuts import render, get_object_or_404
import json

def main(request):
    person = get_object_or_404(Person, pk=1)
    f = open('gen_info/fixtures/mydata.json','r')
    json_data = json.loads(f.read())
    f.close()
    bio_dict = json_data[0][u'fields'][u'bio']
    contacts_dict = json_data[0][u'fields'][u'contacts']
    context = {'person': person, 'bio_dict': bio_dict, 'contacts_dict': contacts_dict}
    return render(request, 'gen_info/main.html', context)
