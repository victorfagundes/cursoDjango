from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.models import User 

urlpatterns = patterns('',
    url('^$','produtos.views.produtos'), 
)
