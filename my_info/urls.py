from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', include('gen_info.urls',
                                          namespace='gen_info')),
                       url(r'^requests', include('http_request_storage.urls',
                                                 namespace='http_requests')),
                       url(r'^settings', include('add_settings.urls',
                                                 namespace='add_settings')),
                       url(r'^edit', include('form_page.urls',
                                                 namespace='form')))                                                 
