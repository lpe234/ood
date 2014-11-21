# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from sho.models import User

# Create your views here.


def show_all(response):
    user_list = User.objects.all()
    if user_list:
        content = {'user_list': user_list}
        render_to_response('xx.html', content)
