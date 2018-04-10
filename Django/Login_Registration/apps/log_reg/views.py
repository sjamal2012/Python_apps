# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.core.urlresolvers import reverse
from django.contrib.messages import error
from datetime import datetime
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

def index(request):
    context = {
        'users':User.objects.all()
    }
    return render(request, 'log_reg/index.html', context)

def register(request):
    result  = User.objects.validate_registration(request.POST)
    if type(result) == list:
        for err in result:
            error(request, err)
        return redirect('/log_reg')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())

        User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password)
        request.session['user_id'] = result.id

    return redirect('/log_reg/logged_in', request.session['context'])

def login(request):
    result = User.objects.validate_login(request.POST)
    if type(result) == list:
        for err in result:
            error(request, err)
        return redirect('/log_reg')
    else:
        request.session['user_id'] = result.id
        return redirect('/log_reg/logged_in')

def logged_in(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')
    context = {
            'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'log_reg/logged_in.html', context)
