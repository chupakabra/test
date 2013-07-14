from form_page.forms import PersonForm
from gen_info.models import Person
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

def init(request):
	person = get_object_or_404(Person, pk=1)
	init_person_form = PersonForm(instance=person)
	photo_path = person.photo_image()
	context = {'person_form': init_person_form, 'photo_path': photo_path}
	return render(request, 'form_page/form.html', context)
	    
def edit(request, template_name = 'form_page/form.html'):
    person = get_object_or_404(Person, pk=1)
    if request.method == 'POST':
        person_form = PersonForm(request.POST, request.FILES, instance=person) 
        if person_form.is_valid(): 
            person_form.save()
            if request.is_ajax():
                return render(request, 'gen_info/main.html')
            else:
                return redirect(reverse('gen_info:main'))
    else:
        person_form = PersonForm()

    return render(request, 'form_page/form.html', {'person_form':person_form})

