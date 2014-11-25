# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from sho import views

__author__ = 'lpe234'
__date__ = '2014-11-20'

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^user/login/', views.login, name='login'),
    url(r'^user/register/', views.register, name='register'),
    url(r'^user/logout/', views.logout, name='logout')
)