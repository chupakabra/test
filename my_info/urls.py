from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^ticket#1', include('gen_info.urls',
                           namespace="gen_info")),
                       url(r'^ticket#3', include('http_request_storage.urls',
                                                 namespace="htpp_requests")))
