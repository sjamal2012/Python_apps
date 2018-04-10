from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime

def index(request):
    return render(request, "session_words/index.html")

def add(request):
    new_word = {}
    for key,value in request.POST.iteritems():
        if key != "csrfmiddlewaretoken" and key !="font":
            new_word[key] = value
        if key == "font":
            new_word['big'] = "big"
    print new_word
    new_word['created_at'] = datetime.now().strftime("%H:%M %p, %B %d, %Y")
    try:
        request.session['session_words']
    except KeyError:
        request.session['session_words'] = []

    temp_list = request.session['session_words']
    temp_list.append(new_word)
    request.session['session_words'] = temp_list
    return redirect('/session_words')

def clear(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/session_words')
