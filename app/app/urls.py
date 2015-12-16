from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'eleme.views.index', name='home'),
    # url(r'^blog/', include('blog.urls')),
#    url(r'',include('eleme.urls')),
    url(r'^login','eleme.views.login',name='login'),
#    url(r'^admin/', include(admin.site.urls)),
)
