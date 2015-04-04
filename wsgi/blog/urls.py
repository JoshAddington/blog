from blog import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
        url(r'^$', views.post_list),
        url(r'^post/(?P<slug>[-\w\d]+)/$' , views.post_detail),
        url(r'^post/new/$', views.post_new, name='post_new'),
        url(r'^post/(?P<slug>[-\w\d]+)/edit/$', views.post_edit, name='post_edit'),
        url(r'^post/(?P<slug>[-\w\d]+)/publish/$', views.post_publish, name='post_publish'),
        url(r'^post/(?P<slug>[-\w\d]+)/delete/$', views.post_delete, name='post_delete'),
        url(r'^post/drafts/$', views.post_draft_list, name='post_draft_list'),
)
