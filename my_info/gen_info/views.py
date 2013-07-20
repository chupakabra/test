from models import Person
from django.shortcuts import render, get_object_or_404
from PIL import Image as PImage
from django.template import RequestContext


def main(request):
    person = get_object_or_404(Person, pk=1)
    img = PImage.open(person.photo.path)
    img.thumbnail((160,160), PImage.ANTIALIAS)
    img.save(img.filename, "PNG")
    context = {'person': person, 'photo': img}
    return render(request, 'gen_info/main.html', context_instance=RequestContext(request, context))
