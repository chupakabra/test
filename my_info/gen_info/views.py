from models import Person
from django.shortcuts import render, get_object_or_404

def main(request):
    person = get_object_or_404(Person, pk=1)
    return render(request, 'gen_info/main.html')
