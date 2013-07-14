from django.conf.urls import patterns, url
from gen_info import views
import django.contrib.auth.views


urlpatterns = patterns('',
                       url(r'^$', views.main, name='main'))

urlpatterns += patterns('django.contrib.auth.views',
	                   (r'^accounts/login/', 'login'))
