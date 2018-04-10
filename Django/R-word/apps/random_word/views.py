# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    request.session['attempt'] = 1
    context = {
    "attempt": request.session['attempt']
    }
    return render(request,"random_word/index.html", context)

def random_word(request):
    rand_word = get_random_string(length=14)
    request.session['attempt'] += 1
    print rand_word
    context = {
    "attempt": request.session['attempt'],
    "rand_word": rand_word
    }
    return render(request,"random_word/word.html", context)
