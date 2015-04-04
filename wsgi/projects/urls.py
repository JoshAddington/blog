from django.conf.urls import patterns, url
from projects import views

urlpatterns = patterns('',
        url(r'^$', views.project_list),
        # url(r'^boroughs/$', views.get_boroughs),
        url(r'^(?P<slug>[-\w\d]+)/$', views.project_detail),
        url(r'^new/$', views.project_new, name='project_new'),
        url(r'^(?P<slug>[-\w\d]+)/edit/$', views.project_edit, name='project_edit'),
        url(r'^(?P<slug>[-\w\d]+)/publish/$', views.project_publish, name='project_publish'),
        url(r'^(?P<slug>[-\w\d]+)/delete/$', views.project_delete, name='project_delete'),
        url(r'^drafts/$', views.project_draft_list, name='project_draft_list'),
)
