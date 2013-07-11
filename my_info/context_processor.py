from django.conf import settings


def settings(request):
    keys = []
    values = []
    for item in dir(settings):
		if item.isupper():
			keys.append(item)
			values.append(getattr(settings, item))
	
    context_extras = dict(map(None,keys,values))
    return context_extras
