from django.conf.urls import patterns, url

from userbase import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<name>[^/]+)/$', views.user, name='user'),
                       
)