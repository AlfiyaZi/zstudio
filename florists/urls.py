___author__ = 'alya'

from django.conf.urls import patterns, url
from florists import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),




)