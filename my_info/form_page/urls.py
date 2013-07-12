from django.conf.urls import patterns, include, url
from form_page import views


urlpatterns = patterns('',
                       url(r'^$', views.form, name='form'))
