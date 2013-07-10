from django.conf.urls import patterns, url
from gen_info import views


urlpatterns = patterns('',
                       url(r'^$', views.main, name='main'))
