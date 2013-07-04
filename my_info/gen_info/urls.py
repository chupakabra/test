from django.conf.urls import patterns, url
from gen_info import views
from gen_info.models import Person

urlpatterns = patterns('',
    url(r'^$', views.main, name='main')
)
