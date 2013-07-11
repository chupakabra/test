from django.conf.urls import patterns, url
from http_request_storage import views

urlpatterns = patterns('',
                       url(r'^$', views.requests, name='requests'))
