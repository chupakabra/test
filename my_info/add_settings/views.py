from django.shortcuts import render
from django.template import RequestContext


def main(request):
	return render(request, 'add_settings/django_settings.html', 
	   context_instance=RequestContext(request))

