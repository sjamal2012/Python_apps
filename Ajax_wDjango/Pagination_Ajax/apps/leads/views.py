# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect, HttpResponse
from .models import Lead
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.core import serializers
from django.core.paginator import Paginator
from django.db.models import Q
from datetime import datetime
import json

LEADS_PER_PAGE = 3

def fetch_leads(request, filt=None):
    return json_leads(filt)

def index(request):
    return render(request, 'leads/index.html')

def filt(request):
    return json_leads(filt=request.POST)

def json_leads(filt=None):
    leads = Lead.objects.all()
    if filt != None:
        if filt["name"] != "":
            leads = leads.filter(Q(first_name__contains=filt["name"]) | Q(last_name__contains=filt["name"]))
        if filt["to"] != "":
            leads = leads.filter(registered_datetime__lt=filt["to"])
        if filt["from"] != "":
            leads = leads.filter(registered_datetime__gt=filt["from"])
    else:
        filt = {"page": 1}

    p = Paginator(leads, LEADS_PER_PAGE)
    serialized = {
        "object_list": serializers.serialize("json", p.page(int(filt["page"])).object_list),
        "pages": range(p.num_pages)
    }
    return HttpResponse(json.dumps(serialized), content_type="application/json")

def add(request):
    return render(request, 'leads/new_lead.html')

def create(request):
    result = Lead.objects.validate_lead_info(request.POST)

    if len(result) > 0:
        for err in result:
            messages.error(request, err)
        return redirect('/add_lead')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        registered_datetime = str(datetime.date)

        Lead.objects.create(first_name=first_name, last_name=last_name, email=email, registered_datetime=registered_datetime)

    return redirect('/')
