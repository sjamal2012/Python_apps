# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, "survey_form/index.html")

def process(request):
    request.session['name'] = request.POST['name']
    request.session['loc'] = request.POST['location']
    request.session['lang'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return redirect('/survey')

def result(request):
    request.session['submits'] += 1
    counter = {
        "submits": request.session['submits']
    }
    return render(request, "survey_form/show.html", counter)
