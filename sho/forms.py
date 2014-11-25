# -*- coding: utf-8 -*-

__author__ = 'lpe234'
__date__ = '2014-11-23'

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label=u'姓名', )
    password = forms.CharField(label=u'密码', widget=forms.PasswordInput)
    remember = forms.BooleanField(label=u'记住密码', required=False)

