from django.conf.urls import patterns, include, url
from django.contrib import admin

from deejCoin.views import *
from userbase import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'deejCoin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
#                       url(r'^$', main_page),
#                       url(r'^login/$', 'django.contrib.auth.views.login'),
#                       url(r'^logout/$', logout_page),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^user/', include('userbase.urls')),
                       url(r'^register/', views.register, name='register'),
)
