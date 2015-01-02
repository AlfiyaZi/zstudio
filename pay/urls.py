__author__ = 'alya'

from django.conf.urls import *

urlpatterns = patterns('',
    url(r'^pay/$', 'pay.views.pay', name='pay'),
    url(r'^pay1/$', 'pay.views.pay', name='pay1'),

)