from django.conf.urls import url, patterns, include

urlpatterns = patterns('',
    url(r'^citibike/', include('citibike.urls'))
)
