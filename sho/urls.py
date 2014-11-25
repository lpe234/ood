# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from sho import views

__author__ = 'lpe234'
__date__ = '2014-11-20'

urlpatterns = patterns('',
    url(r'', views.login, name='index')
)