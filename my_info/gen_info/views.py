from gen_info.models import *
from django.shortcuts import render, get_object_or_404

def main(request):
    person = get_object_or_404(Person, pk=1)
    contacts = get_object_or_404(Contacts, person=person)
    context = {'person': person, 'contacts': contacts}
    return render(request, 'gen_info/main.html', context)
