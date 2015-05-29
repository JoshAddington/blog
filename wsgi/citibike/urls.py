from citibike import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
        # api
        url(r'^api/v1/stations/$', views.station_collection),
        url(r'^api/v1/stations/(?P<pk>[0-9]+)$', views.station_element),
        url(r'^api/v1/updates/$', views.update_collection),
)
