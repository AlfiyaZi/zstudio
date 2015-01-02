___author__ = 'alya'

from django.conf.urls import patterns, url
from about import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^delivery/', views.delivery , name='delivery'),




)