from citibike import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
        # api
        url(r'^api/v1/stations/$', views.station_collection),
        url(r'^api/v1/stations/bikes/$', views.station_bikes_collection),
        url(r'^api/v1/stations/(?P<pk>[0-9]+)$', views.station_element),
        url(r'^api/v1/stations/(?P<pk>[0-9]+)/bikes/$', views.station_bikes),
        url(r'^api/v1/timeline/$', views.timeline_collection),
        url(r'^api/v1/timeline/(?P<date>[0-9-]+)$', views.timeline_date),
        url(r'^api/v1/bikes/$', views.bike_collection),
)
