from django.conf.urls import patterns, url

from userbase import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<name>[^/]+)/$', views.user, name='user'),
                       url(r'^(?P<name>[^/]+)/level_up$', views.level_up, name='level_up'),
                       url(r'^(?P<name>[^/]+)/transaction/$', views.create_transaction, name='transaction')

)
