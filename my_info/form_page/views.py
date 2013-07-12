from forms import PersonForm
from django.shortcuts import render


def form(request):
    context = {'modelform': PersonForm}
    return render(request, 'form_page/form.html', context)
