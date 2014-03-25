from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dashboard.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^home', 'viz.views.getH2Sconc', name='home'),
    url(r'^$', 'viz.views.getH2Sconc', name='map'),
    url(r'^admin/', include(admin.site.urls)),
)
