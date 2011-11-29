from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.models import User 

urlpatterns = patterns('',
    url('^$','blog.views.posts'), 
    url('^post/(?P<id>\d+)\.html$','blog.views.post'), 
)
