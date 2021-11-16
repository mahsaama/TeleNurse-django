# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from apps.users.models import CustomUser
from apps.home.models import Ad
from django.shortcuts import render
import datetime


@login_required(login_url="/login/")
def index(request):
    context = {"segment": "index"}
    html_template = loader.get_template("home/index.html")
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        load_template = request.path.split("/")[-1]
        if load_template == "admin":
            return HttpResponseRedirect(reverse("admin:index"))
        elif load_template == "nurse-list.html":
            return list_of_nurses(request)
        elif load_template == "ads-list.html":
            return list_of_ads(request)

        context["segment"] = load_template
        html_template = loader.get_template("home/" + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:
        html_template = loader.get_template("home/page-404.html")
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template("home/page-500.html")
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def list_of_nurses(request):
    nurses = [nurse for nurse in CustomUser.objects.all()]
    return render(request, "home/nurse-list.html", {"nurses": nurses})


@login_required(login_url="/login/")
def list_of_ads(request):
    # ads = [ad for ad in Ad.objects.all()]

    ad1 = Ad(first_name="user1", last_name="kh1", phone_number="09136875776",
                 address="khaghani", start_time=datetime.datetime.now(), end_time=datetime.datetime.now(), 
                 service_type='1', sex="woman")

    ad2 = Ad(first_name="user2", last_name="kh2", phone_number="09136775776",
                 address="khaghani", start_time=datetime.datetime.now(), end_time=datetime.datetime.now(), 
                 service_type='3', sex="man")

    ad3 = Ad(first_name="user3", last_name="kh3", phone_number="09136675776",
                 address="khaghani", start_time=datetime.datetime.now(), end_time=datetime.datetime.now(), 
                 service_type='2', sex="woman")

    ads = [ad1, ad2, ad3]
    context = {'ads': ads}

    # return render(request, "home/ads-list.html", context)
    return render(request, "home/ads.html", context)
