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
    return render(request, 'login_reg/index.html', context)

def register(request):
    errors = User.objects.validate_registration(request.POST)
    if errors:
        for err in errors:
            error(request, err)
        return redirect('/login_reg')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())

        User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password)

    context = {
        'user': User.objects.get(email=email)
    }
    return redirect('/log_reg/logged_in')

def login(request):
    errors = User.objects.validate_login(request.POST)
    if errors:
        for err in errors:
            error(request, err)
        return redirect('/login_reg')
    else:
        return redirect('/login_reg/logged_in', user=user)

def logged_in(request, user_id):
    context = {
        'user':User.objects.get(id=user_id)
    }
    return render(request, 'login_reg/logged_in.html', context)
