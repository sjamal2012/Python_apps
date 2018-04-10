from __future__ import unicode_literals

from products import items
from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
import random


def index(request):
    try:
        request.session['gold']
    except KeyError:
        request.session['gold'] = 0

    try:
        request.session['activities']
    except KeyError:
        request.session['activities'] = []

    return render(request, "ninja_gold/index.html")

def process(request, building_id):

    if int(building_id) == 1:
        gold = random.randrange(10,21)
        request.session['gold'] += gold
        request.session['building'] = "farm"
        request.session['activities'].append({'activity': "farm", 'gold':gold, 'time': datetime.now().strftime("%Y/%m/%d %I:%M %p")})
    elif int(building_id) == 2:
        gold = random.randrange(5,11)
        request.session['gold'] += gold
        request.session['building'] = "cave"
        request.session['activities'].append({'activity': "cave", 'gold':gold, 'time': datetime.now().strftime("%Y/%m/%d %I:%M %p")})
    elif int(building_id) == 3:
        gold = random.randrange(2,6)
        request.session['gold'] += gold
        request.session['building'] = "house"
        request.session['activities'].append({'activity': "house", 'gold':gold, 'time': datetime.now().strftime("%Y/%m/%d %I:%M %p")})
    elif int(building_id) == 4:
        gold = random.randrange(-50,51)
        request.session['gold'] += gold
        request.session['building'] = "casino"
        request.session['activities'].append({'activity': "casino", 'gold':gold, 'time': datetime.now().strftime("%Y/%m/%d %I:%M %p")})


    return redirect('/ninja_gold')

def reset(request):
    del request.session['gold']
    del request.session['activities']
    return redirect('/ninja_gold')
