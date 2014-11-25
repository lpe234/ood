# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.context_processors import csrf

from sho.models import User
from sho.forms import LoginForm

# Create your views here.


def show_all(request):
    user_list = User.objects.all()
    if user_list:
        content = {'user_list': user_list}
        render_to_response('xx.html', content)


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['user_name']
            password = form.cleaned_data['password']
            is_remind = form.cleaned_data['remind_pass']
            print name, password, is_remind
            return HttpResponse('hi {0}'.format(name))
    else:
        form = LoginForm()
    context = {'form': form}
    context.update(csrf(request))
    return render_to_response('sho/login.html', context)