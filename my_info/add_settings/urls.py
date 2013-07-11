from django.conf.urls import patterns, url
from add_settings import views

urlpatterns = patterns('',
                       url(r'^$', views.main, name='settings'))
