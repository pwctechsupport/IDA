from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.conf import settings as django_settings
from django.http import JsonResponse
from django.shortcuts import redirect
from django import forms
from .models import Contactus
from datetime import datetime
import json
import base64
import os, pandas as pd
import html
import mimetypes
import numpy as np
import math

# Create your views here.
def firstconstructor(request):
	firstname = ""
	# request.session['firstname'] = "user"
	if 'firstname' in request.session:
		firstname = request.session['firstname']
	return firstname

def constructor(request):
	username = ""
	# request.session['name'] = "userhero"
	if 'name' in request.session:
		username = request.session['name']
	return username

def welcomeconstructor(request):
	welcome = ""
	# request.session['name'] = "userhero"
	if 'welcomename' in request.session:
		welcome = request.session['welcomename']
	return welcome

def contact(request, *args, **kwargs):
	firstname = firstconstructor(request);
	username = constructor(request);
	context = {"firstname":firstname}
	welcome = welcomeconstructor(request);

	if(welcome==""):
		return render(request,'welcome.html',context)
	else:
		if not(username==""):
			context = {"username":username}
		return render(request,'contact.html',context)


@csrf_protect
def submitContact(request):
	username = constructor(request);
	body_unicode = request.body.decode('utf-8')
	received_json = json.loads(body_unicode)
	name = received_json["name"]
	job = received_json["job"]
	company = received_json["company"]
	email = received_json["email"]

	# filename= name+"_"+job+"_"+company
	# # print(django_settings.STATICFILES_DIRS[0])
	# file=open(django_settings.STATICFILES_DIRS[0]+f'\\SubmitContact\\{filename}.txt','w')
	# # print()
	# toFile = "Name: "+name+"\nJob: "+job+"\nCompany: "+company+"\nEmail: "+email+""
	# file.write(toFile)
	# file.close()
	foo_instance = Contactus.objects.create(name=name,job=job,company=company,email=email, submittime=datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
	json_response = {"return":"success"}
	return JsonResponse(json_response)
