from django.conf.urls import patterns, url
from http_request_storage import views

urlpatterns = patterns('',
                       url(r'^$', views.main, name='main'),
                       url(r'^requests', views.requests, name='requests'))
