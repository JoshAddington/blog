from openshift import views
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from openshift import settings
admin.autodiscover()

urlpatterns = patterns('',
        url(r'^', include('blog.urls')),
        url(r'^about/$', views.about),
        url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
        url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
        url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
        url(r'^admin/', include(admin.site.urls)),
        url(r'^boroughs/', views.boroughs),
        url(r'^contact/$', views.contact),
        url(r'^projects/', include('projects.urls')),
        url(r'^citibike/', include('citibike.urls')),
        url('', include('django.contrib.auth.urls', namespace='auth')),
)
