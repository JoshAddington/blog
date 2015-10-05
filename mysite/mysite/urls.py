from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from . import settings
from . import views
admin.autodiscover()

urlpatterns = patterns('',
        url(r'^', include('blog.urls')),
        url(r'^projects/', include('projects.urls')),
        url(r'^api/', include('api.urls')),
        url(r'^about/$', views.about),
        url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
        url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
        url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
        url(r'^admin/', include(admin.site.urls)),
        url(r'^contact/$', views.contact),
        # url(r'^citibike/', include('citibike.urls')),
        url('', include('django.contrib.auth.urls', namespace='auth')),
)
