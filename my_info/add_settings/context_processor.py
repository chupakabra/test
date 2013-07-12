from django.conf import settings


def settings_processor(request):
    context_extras = dict((k, getattr(settings, k)) for k in dir(settings)
                      if k.isupper())

    return {'settings': context_extras}
