from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', include('gen_info.urls', namespace="gen_info")),
    url(r'^$', include('http_request_storage.urls', namespace="htpp_requests")),
    # Examples:
    # url(r'^$', 'my_info.views.home', name='home'),
    # url(r'^my_info/', include('my_info.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
