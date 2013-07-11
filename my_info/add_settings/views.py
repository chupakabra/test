from django.shortcuts import render
from django.template import RequestContext
from context_processor import settings_processor


def main(request):
	return render(request, 'add_settings/django_settings.html', 
	   context_instance=RequestContext(request, processors=[settings_processor]))

