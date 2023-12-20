from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.conf import settings as django_settings
from django.http import JsonResponse
from django.shortcuts import redirect
from django.utils.timezone import now
from django.db import connection
from django import forms
from .models import Userlogin, LoginAttempt
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

#temporary, delete if it officially deployed
def FirstLogin(request, *args, **kwargs):
	username = constructor(request);
	welcome = welcomeconstructor(request);
	context = {"username":username}
	if(welcome==""):
		return render(request,'welcome.html',context)
	else:
		return render(request,'FirstLogin.html',context)

def TrialEnd(request):
	# with connection.cursor() as cursor:
	# 	cursor.execute("SELECT TrialEnd FROM TrialTable")
	# 	row = cursor.fetchone()
	# 	if row[0] <= now() :
	# 		return HttpResponse(status=401)
	# return JsonResponse({"trialend": True})
	return JsonResponse({"trialend": False})

@csrf_protect
@ratelimit(key='ip', rate='5/m', method='POST', block=True)
def doLogin(request):
	json_loads=json.loads(request.body.decode('utf-8'))
	username = json_loads['username']
	password = json_loads['password']
	welcome = welcomeconstructor(request);
	# check login attempt
	print(username, password)
	attempt = LoginAttempt.objects.filter(username=username).first()
	if (attempt != None and attempt.lastattempt + timedelta(minutes=5) <= now()):
		attempt.delete()
		attempt = None
	if (attempt != None and attempt.count >= 5 and attempt.lastattempt + timedelta(minutes=5) > now()):
		return JsonResponse({"username":"", "message":"attempt"})	

	print(attempt)
	#encryptPassword = password.encode("utf-8")
	key = "this is a key123this is a key123"
	cipher = AES.new(key.encode('utf8'),AES.MODE_GCM) #AES.MODE_GCM)
	ciphertext, tag = cipher.encrypt_and_digest(bytes(password ,'utf8'))

	encoded = base64.b64encode(ciphertext)
	data = list(Userlogin.objects.filter(username=username).values('username','password'))
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
			t = Userlogin.objects.get(username=username)	
			t.lastlogin = datetime.today().strftime('%Y-%m-%d %H:%M:%S')  # change field
			t.save() # this will update only
			request.session['name'] = username
			request.session.set_expiry(30000)
			request.session.SESSION_EXPIRE_AT_BROWSER_CLOSE = True
			request.session['firstname'] = username
			request.session['name'] = username
			# remove login attempt
			LoginAttempt.objects.filter(username=username).delete()
			
			return JsonResponse({"username":username, "message":"success"})
	
	# login failed, create login attempt

	if (attempt == None):
		attempt = LoginAttempt(username=username, count=0, lastattempt=now())
		
	attempt.count = attempt.count + 1
	attempt.lastattempt = now()
	attempt.save()

	return JsonResponse({ "username":"", "message": "failed"})


def changepassword(request, *args, **kwargs): #fak: coba bikin function changepassword
	firstname = firstconstructor(request);
	username = constructor(request);
	welcome = welcomeconstructor(request);
	context = {"firstname":firstname}

	if(welcome==""):
		return render(request,'welcome.html')
	else:
		if not(username==""):
			context = {"username":username}
			return render(request,'changepassword.html',context)
		else:
			return render(request,'home.html',context)
	
@csrf_protect
def doChangePassword(request):
	username = constructor(request);
	# username = request.POST.get('username', '') #oke jalan

	json_loads=json.loads(request.body.decode('utf-8'))
	password = json_loads['currentpassword']
	welcome = welcomeconstructor(request);
	# password = request.POST.get('currentpassword', '') #oke jalan

	# encryptcurrentpassword = password.encode("utf-8")
	# encoded = base64.b64encode(encryptcurrentpassword)
    
	newpassword = json_loads['newpassword']
	# newpassword = request.POST.get('newpassword', '') #oke jalan
    
	confirmpassword = json_loads['confirmpassword']
	# confirmpassword = request.POST.get('confirmpassword', '') #oke jalan

	try:
		#cari dulu apakah si passwordnya ada di database apa enggak
		data = list(Userlogin.objects.filter(username=username).values('username','password'))

		message=""
		if(len(data)>0):
			#kalo ada yaudah, cek lagi new ama confirm passwordnya sama ga

			_, nonce, tag, hash = data[0]['password'].split('$',3)
			ciphertext=base64.b64decode(hash)
			nonce=base64.b64decode(nonce)
			tag=base64.b64decode(tag)   
						
			key = "this is a key123this is a key123".encode('utf8')
			cipher = AES.new(key,AES.MODE_GCM,nonce=nonce)
				
			decoded = cipher.decrypt_and_verify(ciphertext, tag)
			decodedpassword = bytes.decode(decoded)
			
			if(password != decodedpassword):
				context = {"username":""}
				message="Current password is incorrect"
			elif(confirmpassword != newpassword):
				#kalo ga match balikin ke home change password
				context = {"username":""}
				message="New password and confirmation password do not match"
			else:
				cipher = AES.new(key, AES.MODE_GCM)
				nonce = cipher.nonce
				ciphertext, tag = cipher.encrypt_and_digest(confirmpassword.encode("utf-8"))
				nonce = base64.b64encode(nonce).decode("utf-8")
				tag = base64.b64encode(tag).decode("utf-8")
				ciphertext = base64.b64encode(ciphertext).decode("utf-8")
				encodedconfirmpassword = f'AES${nonce}${tag}${ciphertext}'

				Userlogin.objects.filter(username=username).update(password=encodedconfirmpassword)
				context = {"username":username}
				message="success"
		else:
			context = {"username":""}
			message="Current password is incorrect"
	except:
		#kalo ga ada didatabase balikin ke home change password
		context = {"username":""}
		message="Please re INPUT your data!"
        

	if(message=="success"):
		#return render(request,'home.html',context)
		json_response = {"return":"success"}
		return JsonResponse(json_response)
	else:
		#return render(request,'changepassword.html',context)
		json_response = {"return":message}
		return JsonResponse(json_response)

def doLogout(request):
	username = constructor(request);
	firstname = firstconstructor(request);
	welcome = welcomeconstructor(request);
	
	if (username==""):
		if(welcome==""):
			return render(request,'welcome.html')
		else:
			return render(request,'home.html')
	else:
		del request.session['name']
		return redirect('Home:home')	

def home(request, *args, **kwargs):
	firstname = firstconstructor(request);
	#firstname = "user"
	username = constructor(request);
	context = {"firstname":firstname}
	welcome = welcomeconstructor(request);

	if(welcome==""):
		return render(request,'welcome.html')
	else:
		if not(username==""):
			context = {"username":username}
		return render(request,'home.html',context)


def copyright(request, *args, **kwargs):
	firstname = firstconstructor(request);
	username = constructor(request);
	context = {"firstname":firstname}
	welcome = welcomeconstructor(request);

	if(welcome==""):
		return render(request,'welcome.html')
	else:
		if not(username==""):
			context = {"username":username}
			return render(request,'copyright.html',context)
		else:
			return render(request,'home.html',context)

def TermOfService(request, *args, **kwargs):
	firstname = firstconstructor(request);
	username = constructor(request);
	context = {"firstname":firstname}
	welcome = welcomeconstructor(request);

	if(welcome==""):
		return render(request,'welcome.html')
	else:
		if not(username==""):
			context = {"username":username}
		return render(request,'TermOfService.html',context)

	
@csrf_protect
def contoh_form_tanpa_file(request):
	body_unicode = request.body.decode('utf-8')
	received_json = json.loads(body_unicode)
	data = received_json["id"] #id ini cuman contoh parameter yg dilempar dr ajax
	json_response = {"return":data}
	return JsonResponse(json_response)