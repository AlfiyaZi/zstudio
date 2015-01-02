__author__ = 'alya'
from django.conf.urls import patterns, url
from contact import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^add_contact/$', views.add_contact, name='add_contact'),





)

