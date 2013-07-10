from django.conf.urls import patterns, url
from http_request_storage import views

urlpatterns = patterns('',
                       url(r'^$', 'http_request_storage/main.html', name='main'),
                       url(r'^requests', views.requests, name='requests'))
