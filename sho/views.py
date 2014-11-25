# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse

import logging
logger = logging.getLogger(__name__)

from sho.models import User
from sho.forms import RegisterForm, LoginForm

# Create your views here.


def index(request):

    # 验证是否登陆，否则跳回登陆页
    username = request.session.get('username', None)
    if not username:
        return HttpResponseRedirect(reverse(login))
    # 获取当前登陆用户信息
    user = User.objects.get(username__exact=username)
    context = {'user': user, }
    return render_to_response('sho/index.html', context)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            User.objects.create(username=username, password=password)
            return HttpResponseRedirect(reverse(login))
    else:
        form = RegisterForm()
    context = {'form': form, }
    context.update(csrf(request))
    return render_to_response('sho/register.html', context)


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            is_remind = form.cleaned_data['remember']
            # 用户登陆验证
            user = None
            logger.debug('attemp to login in name {0} password {1}'.format(username, password))
            try:
                user = User.objects.get(username__exact=username, password__exact=password)
            except(User.DoesNotExist, ):
                pass
            if user:
                # 登陆成功，设置cookie及session
                response = HttpResponseRedirect(reverse(index))
                response.set_cookie('username', value=user.username, max_age=60*60*24*7)
                response.set_cookie('password', value=user.password, max_age=60*60*24*7)
                request.session['username'] = user.username
                return response
            else:
                return HttpResponseRedirect(reverse(login))
    else:
        form = LoginForm()
    context = {'form': form}
    context.update(csrf(request))
    return render_to_response('sho/login.html', context)


def logout(request):
    return None