from . import views
from django.conf.urls import url, patterns

urlpatterns = patterns('',
    url(r'^boroughs/$', views.boroughs),
    url(r'^map/$', views.citibike_map),
    url(r'^stations/$', views.station_collection),
    url(r'^stations/(?P<pk>[0-9]+)/$', views.station_detail),
    url(r'^stations/(?P<pk>[0-9]+)/bikes$', views.station_bikes),
    url(r'^updates/$', views.updates),
)
