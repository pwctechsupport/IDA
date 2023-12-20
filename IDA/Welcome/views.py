from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.conf import settings as django_settings
from django.http import JsonResponse
from django.shortcuts import redirect
from django.utils.timezone import now
from django.db import connection
from django import forms
from .models import WelcomeUserlogin, WelcomeLoginAttempt
from datetime import datetime, timedelta
import json
import base64
import os, pandas as pd
import html
import mimetypes
import numpy as np
import math
from Crypto.Cipher import AES
from django_ratelimit.decorators import ratelimit

#temporary, delete if it officially deployed
# def firstconstructor(request):
# 	firstname = ""
# 	# request.session['firstname'] = "user"
# 	if 'firstname' in request.session:
# 		firstname = request.session['firstname']
# 	return firstname

def constructor(request):
	username = ""
	# request.session['name'] = "userhero"
	if 'welcomename' in request.session:
		username = request.session['welcomename']
	return username

#temporary, delete if it officially deployed
def WelcomeFirstLogin(request, *args, **kwargs):
	username = constructor(request);
	context = {"welcomename":username}
	print('welcomeFirstLogin ',username)
	return render(request,'Welcome.html',context)

@csrf_protect
@ratelimit(key='ip', rate='5/m', method='POST', block=True)
def welcomeLogin(request):
	json_loads=json.loads(request.body.decode('utf-8'))
	username = json_loads['username']
	password = json_loads['password']
	print('user pass  ',username, password)
	# check login attempt
	attempt = WelcomeLoginAttempt.objects.filter(username=username).first()
	print('attempt: ',attempt)
	if (attempt != None and attempt.lastattempt + timedelta(minutes=5) <= now()):
		attempt.delete()
		attempt = None
	if (attempt != None and attempt.count >= 5 and attempt.lastattempt + timedelta(minutes=5) > now()):
		return JsonResponse({"username":"", "message":"attempt"})	

	#encryptPassword = password.encode("utf-8")
	key = "this is a key123this is a key123"
	cipher = AES.new(key.encode('utf8'),AES.MODE_GCM) #AES.MODE_GCM)
	ciphertext, tag = cipher.encrypt_and_digest(bytes(password ,'utf8'))

	encoded = base64.b64encode(ciphertext)
	print(username, password)
	data = list(WelcomeUserlogin.objects.filter(username=username).values('username','password'))
	print('data: ',data)
	message=""
	if(len(data)>0):
		_, nonce, tag, hash = data[0]['password'].split('$',3)
		ciphertext=base64.b64decode(hash)
		nonce=base64.b64decode(nonce)
		tag=base64.b64decode(tag)   
					
		key = "this is a key123this is a key123"
		cipher = AES.new(key.encode('utf8'),AES.MODE_GCM,nonce=nonce)
			
		decoded = cipher.decrypt_and_verify(ciphertext, tag)
		decodedpassword = bytes.decode(decoded)
		
		if(password == decodedpassword):
			t = WelcomeUserlogin.objects.get(username=username)	
			t.lastlogin = datetime.today().strftime('%Y-%m-%d %H:%M:%S')  # change field
			t.save() # this will update only
			request.session['welcomename'] = username
			request.session.set_expiry(30000)
			request.session.SESSION_EXPIRE_AT_BROWSER_CLOSE = True
			request.session['welcomefirstname'] = username
			request.session['welcomename'] = username
			print('request',request)
			print('session',request.session['welcomename'])
			# remove login attempt
			WelcomeLoginAttempt.objects.filter(username=username).delete()

			return JsonResponse({"username":username, "message":"success"})
	
	# login failed, create login attempt

	if (attempt == None):
		attempt = WelcomeLoginAttempt(username=username, count=0, lastattempt=now())
		
	attempt.count = attempt.count + 1
	attempt.lastattempt = now()
	attempt.save()

	return JsonResponse({ "username":"", "message": "failed"})
