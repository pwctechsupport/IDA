from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.conf import settings as django_settings
from django.http import JsonResponse
from django.shortcuts import redirect
from django import forms
from .other_py import print_hello
from .knnclas import calculate_knnclas
from .knnregr import calculate_knnregr
from .regression import calculate_linear_regression
from .log_regression_classification import calculate_logistic_regression_classification
from .polynomial_regression import calculate_polynomial_regression
from .svr import calculate_svr
from .svm import calculate_svm
from .arima import calculate_arima
from .random_forest_regression import rf_regression
from .RF_classification import rf_class
from .kmeans import calculate_kmeans
from .mbkmeans import calculate_mbkmeans
from .agglomerative import calculate_agglomerative
from .spectral_clustering import calculate_spectral
from .dectree import calculate_dectree
from .dec_tree_regression import calculate_dectree_regress
from .BIRCH import birch_cluster
from .dbscan import dbscan_cluster
from .trend import see_trend
from .trend_line import line_trend
from .trend_bar import bar_trend
from .trend_scatter import scatter_trend
from .trend_hist import hist_trend
from .trend_stat import stat_trend
from datetime import datetime
import json
import base64
import os, pandas as pd
import html
import mimetypes
import numpy as np
import math
from .models import Chatlist
from Home.models import AuthUser
from django.utils.html import escape, format_html
from django.utils.safestring import mark_safe
from django.template import loader

# Create your views here.
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

def chat(request, *args, **kwargs):
	firstname = firstconstructor(request);
	username = constructor(request);
	context = {"firstname":firstname}
	welcome = welcomeconstructor(request);
	
	if(welcome==""):
		return render(request,'welcome.html',context)
	else:
		if not(username==""):
			context = {"username":username}
			return render(request,'chat.html',context)
		else:
			return render(request,'home.html',context)


@csrf_protect
def downloadtemplate(request, *args, **kwargs):
	username = constructor(request);
	mltype = request.POST['mltype']
	# mltype = "Cluster"
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	if(mltype == "Cluster" or mltype == "Trend"):
		filename = 'Clustering_Template.xlsx'
	elif(mltype == "Probability"):
		filename = 'Classification_Template.xlsx'
	elif(mltype == "Regression"):
		filename = 'Regression_Template.xlsx'
	filepath = BASE_DIR + '/static/files/' + filename
	path = open(filepath, 'rb')
	mime_type, _ = mimetypes.guess_type(filepath)
	template = HttpResponse(path, content_type=mime_type)
	template['Content-Disposition'] = "attachment; filename=%s" % filename
	template['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
	return template

@csrf_protect
def downloadsample(request, *args, **kwargs):
	username = constructor(request);
	mltype = request.POST['mltype']
	# mltype = "Cluster"
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	if(mltype == "Cluster" or mltype == "Trend"):
		filename = 'Clustering_Sample.xlsx'
	elif(mltype == "Probability"):
		filename = 'Classification_Sample.xlsx'
	elif(mltype == "Regression"):
		filename = 'Regression_Sample.xlsx'
	filepath = BASE_DIR + '/static/files/' + filename
	path = open(filepath, 'rb')
	mime_type, _ = mimetypes.guess_type(filepath)
	template = HttpResponse(path, content_type=mime_type)
	template['Content-Disposition'] = "attachment; filename=%s" % filename
	template['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
	return template


@csrf_protect
def viewMore(request):
	username = constructor(request);
	data = request.FILES.get('file')
	algoType = request.POST['algoType']
	mltype = request.POST['mltype']

	issample = request.POST['issample']
	list_table = pd.DataFrame();
	resultColumn = []
	df = pd.DataFrame()
	if issample=="1":
		BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		if(mltype == "Cluster" or mltype == "Trend"):
			filename = 'Clustering_Sample.xlsx'
		elif(mltype == "Probability"):
			filename = 'Classification_Sample.xlsx'
		elif(mltype == "Regression"):
			filename = 'Regression_Sample.xlsx'
		filepath = BASE_DIR + '/static/files/' + filename
		df = pd.read_excel(filepath)
	else:
		filename = str(data)
		if(filename.endswith(".xlsx") or filename.endswith(".xls")):
			df = pd.read_excel(data)
		else:
			df = pd.read_csv(data,delimiter="|")
	list_table = df
		# print(df)

	#set a column that ends with a null as the y variable
	y_var=list_table.loc[:, list_table.iloc[-1].isna()]
	#union y column with previous dataset to set y as the first column
	list_table= pd.concat([y_var,list_table], axis=1)
	#drop duplicate y column
	list_table = list_table.loc[:,~list_table.columns.duplicated()]

	column_length = list_table.shape[1]
	if(mltype == "Regression"):
		if list_table.shape[1]>5:
				list_table.drop(list_table.iloc[:,5:list_table.shape[1]], axis=1, inplace=True)
		list_table.iloc[:,2:column_length] = list_table.iloc[:,2:column_length].fillna(method='ffill')
	elif(mltype == "Probability"):
		if list_table.shape[1]>5:
				list_table.drop(list_table.iloc[:,5:list_table.shape[1]], axis=1, inplace=True)	
		list_table.iloc[:,2:column_length] = list_table.iloc[:,2:column_length].fillna(method='ffill')		
	elif(mltype == "Cluster"):
		if list_table.shape[1]>3:
				list_table.drop(list_table.iloc[:,3:list_table.shape[1]], axis=1, inplace=True)
		list_table.iloc[:,0:column_length] = list_table.iloc[:,0:column_length].fillna(method='ffill')
    # else:
    # 	if list_table.shape[1]>3:
    #     		list_table.drop(list_table.iloc[:,3:list_table.shape[1]], axis=1, inplace=True)


	column_length = list_table.shape[1]
	listOriginalColumn = list_table.columns.values.tolist()
	columnList = pd.DataFrame (listOriginalColumn, columns = ['column_name'])
	
	for i in range(column_length):
		list_table = list_table.rename(columns={ list_table.columns[i]: "value"+str(i+1) })

	#to be developed in v2
	# categorical = list_table.select_dtypes(exclude = ['float64','int64','int'])
	# numerical = list_table.select_dtypes(include=['float64','int64','int'])
	
	# if(mltype == "Regression"):
	# 	if not categorical.empty:
	# 		categorical_df = pd.get_dummies(categorical)
	# 		list_table = pd.concat([categorical_df, numerical], axis = 1)

	resultcalculation = pd.DataFrame()
	accuracyResult = pd.DataFrame()
	listColumnResult = list_table.columns.values.tolist()
	pdColumnResult = pd.DataFrame (listOriginalColumn, columns = ['column_name'])

	if(algoType == "Linear Regression"):
		resultcalculation, accuracyResult, resultmatrix = calculate_linear_regression(list_table,pdColumnResult,1)
		# resultmatrix = ""
		#column name follow from uploaded data
		resultColumn = resultcalculation.columns.values.tolist()
		resultColumn = pd.DataFrame (resultColumn, columns = ['column_name'])
		accuracyColumn = accuracyResult.columns.values.tolist()
		accuracyColumn = pd.DataFrame (accuracyColumn, columns = ['column_name'])
		context = {"username":username, 'Algo':algoType,'result':resultcalculation, 'accuracy':accuracyResult, 'resultColumn':resultColumn, 'accuracyColumn':accuracyColumn, 'add':resultmatrix }
		return render(request,"regression_popup.html",context)
	elif(algoType == "ARIMA"):
		resultcalculation, accuracyResult, resultmatrix = calculate_arima(list_table,pdColumnResult,1)
		resultColumn = resultcalculation.columns.values.tolist()
		resultColumn = pd.DataFrame (resultColumn, columns = ['column_name'])
		accuracyColumn = accuracyResult.columns.values.tolist()
		accuracyColumn = pd.DataFrame (accuracyColumn, columns = ['column_name'])
		context = {"username":username, 'Algo':algoType,'result':resultcalculation, 'accuracy':accuracyResult, 'resultColumn':resultColumn, 'accuracyColumn':accuracyColumn, 'add':resultmatrix }
		return render(request,"regression_popup.html",context)
	elif(algoType == "Polynomial Regression"):
		resultcalculation, accuracyResult, resultmatrix = calculate_polynomial_regression(list_table,pdColumnResult,1)
		resultColumn = resultcalculation.columns.values.tolist()
		resultColumn = pd.DataFrame (resultColumn, columns = ['column_name'])
		accuracyColumn = accuracyResult.columns.values.tolist()
		accuracyColumn = pd.DataFrame (accuracyColumn, columns = ['column_name'])
		context = {"username":username, 'Algo':algoType,'result':resultcalculation, 'accuracy':accuracyResult, 'resultColumn':resultColumn, 'accuracyColumn':accuracyColumn, 'add':resultmatrix }
		return render(request,"regression_popup.html",context)
	elif(algoType == "Support Vector Machines Regression"):
		resultcalculation, accuracyResult, resultmatrix = calculate_svr(list_table,pdColumnResult,1)
		resultColumn = resultcalculation.columns.values.tolist()
		resultColumn = pd.DataFrame (resultColumn, columns = ['column_name'])
		accuracyColumn = accuracyResult.columns.values.tolist()
		accuracyColumn = pd.DataFrame (accuracyColumn, columns = ['column_name'])
		context = {"username":username, 'Algo':algoType,'result':resultcalculation, 'accuracy':accuracyResult, 'resultColumn':resultColumn, 'accuracyColumn':accuracyColumn, 'add':resultmatrix }
		return render(request,"regression_popup.html",context)
	elif(algoType == "Random Forest Regression"):
		resultcalculation, accuracyResult, resultmatrix = rf_regression(list_table,pdColumnResult,1)
		resultColumn = resultcalculation.columns.values.tolist()
		resultColumn = pd.DataFrame (resultColumn, columns = ['column_name'])
		accuracyColumn = accuracyResult.columns.values.tolist()
		accuracyColumn = pd.DataFrame (accuracyColumn, columns = ['column_name'])
		context = {"username":username, 'Algo':algoType,'result':resultcalculation, 'accuracy':accuracyResult, 'resultColumn':resultColumn, 'accuracyColumn':accuracyColumn, 'add':resultmatrix }
		return render(request,"regression_popup.html",context)
	elif(algoType == "K-nearest Neighbour Regression"):
		resultcalculation, accuracyResult, resultmatrix = calculate_knnregr(list_table,pdColumnResult,1)
		resultColumn = resultcalculation.columns.values.tolist()
		resultColumn = pd.DataFrame (resultColumn, columns = ['column_name'])
		accuracyColumn = accuracyResult.columns.values.tolist()
		accuracyColumn = pd.DataFrame (accuracyColumn, columns = ['column_name'])
		context = {"username":username, 'Algo':algoType,'result':resultcalculation, 'accuracy':accuracyResult, 'resultColumn':resultColumn, 'accuracyColumn':accuracyColumn, 'add':resultmatrix }
		return render(request,"regression_popup.html",context)
	elif(algoType == "Decision Tree Regression"):
		resultcalculation, accuracyResult, resultmatrix = calculate_dectree_regress(list_table,pdColumnResult,1)
		resultColumn = resultcalculation.columns.values.tolist()
		resultColumn = pd.DataFrame (resultColumn, columns = ['column_name'])
		accuracyColumn = accuracyResult.columns.values.tolist()
		accuracyColumn = pd.DataFrame (accuracyColumn, columns = ['column_name'])
		context = {"username":username, 'Algo':algoType,'result':resultcalculation, 'accuracy':accuracyResult, 'resultColumn':resultColumn, 'accuracyColumn':accuracyColumn, 'add':resultmatrix }
		return render(request,"regression_popup.html",context)
	elif(algoType == "K-nearest Neighbour Class"):
		accuracyResult, resultcalculation = calculate_knnclas(list_table,pdColumnResult,1)
		resultmatrix = ""
		resultColumn = resultcalculation.columns.values.tolist()
		resultColumn = pd.DataFrame (resultColumn, columns = ['column_name'])
		accuracyColumn = accuracyResult.columns.values.tolist()
		accuracyColumn = pd.DataFrame (accuracyColumn, columns = ['column_name'])
		context = {"username":username, 'Algo':algoType,'result':resultcalculation, 'accuracy':accuracyResult, 'resultColumn':resultColumn, 'accuracyColumn':accuracyColumn, 'add':resultmatrix }
		return render(request,"classification_popup.html",context)
	elif(algoType == "Decision Tree"):
		accuracyResult, resultcalculation = calculate_dectree(list_table,pdColumnResult,1)
		resultmatrix = ""
		resultColumn = resultcalculation.columns.values.tolist()
		resultColumn = pd.DataFrame (resultColumn, columns = ['column_name'])
		accuracyColumn = accuracyResult.columns.values.tolist()
		accuracyColumn = pd.DataFrame (accuracyColumn, columns = ['column_name'])
		context = {"username":username, 'Algo':algoType,'result':resultcalculation, 'accuracy':accuracyResult, 'resultColumn':resultColumn, 'accuracyColumn':accuracyColumn, 'add':resultmatrix }
		return render(request,"classification_popup.html",context)
	elif(algoType == "Logistic Regression Classification"):
		accuracyResult, resultcalculation = calculate_logistic_regression_classification(list_table,pdColumnResult,1)
		resultmatrix = ""
		resultColumn = resultcalculation.columns.values.tolist()
		resultColumn = pd.DataFrame (resultColumn, columns = ['column_name'])
		accuracyColumn = accuracyResult.columns.values.tolist()
		accuracyColumn = pd.DataFrame (accuracyColumn, columns = ['column_name'])
		context = {"username":username, 'Algo':algoType,'result':resultcalculation, 'accuracy':accuracyResult, 'resultColumn':resultColumn, 'accuracyColumn':accuracyColumn, 'add':resultmatrix }
		return render(request,"classification_popup.html",context)
	elif(algoType == "Random Forest Classification"):
		accuracyResult, resultcalculation = rf_class(list_table,pdColumnResult,1)
		resultmatrix = ""
		resultColumn = resultcalculation.columns.values.tolist()
		resultColumn = pd.DataFrame (resultColumn, columns = ['column_name'])
		accuracyColumn = accuracyResult.columns.values.tolist()
		accuracyColumn = pd.DataFrame (accuracyColumn, columns = ['column_name'])
		context = {"username":username, 'Algo':algoType,'result':resultcalculation, 'accuracy':accuracyResult, 'resultColumn':resultColumn, 'accuracyColumn':accuracyColumn, 'add':resultmatrix }
		return render(request,"classification_popup.html",context)
	elif(algoType == "Support Vector Machines Classification"):
		accuracyResult, resultcalculation = calculate_svm(list_table,pdColumnResult,1)
		resultmatrix = ""
		resultColumn = resultcalculation.columns.values.tolist()
		resultColumn = pd.DataFrame (resultColumn, columns = ['column_name'])
		accuracyColumn = accuracyResult.columns.values.tolist()
		accuracyColumn = pd.DataFrame (accuracyColumn, columns = ['column_name'])
		context = {"username":username, 'Algo':algoType,'result':resultcalculation, 'accuracy':accuracyResult, 'resultColumn':resultColumn, 'accuracyColumn':accuracyColumn, 'add':resultmatrix }
		return render(request,"classification_popup.html",context)
	elif(algoType == "K-Means"):
		resultcalculation, resultmatrix = calculate_kmeans(list_table,pdColumnResult,1)
		accuracyResult = pd.DataFrame()
		resultColumn = resultcalculation.columns.values.tolist()
		resultColumn = pd.DataFrame (resultColumn, columns = ['column_name'])
		accuracyColumn = accuracyResult.columns.values.tolist()
		accuracyColumn = pd.DataFrame (accuracyColumn, columns = ['column_name'])
		context = {"username":username, 'Algo':algoType,'result':resultcalculation, 'accuracy':accuracyResult, 'resultColumn':resultColumn, 'accuracyColumn':accuracyColumn, 'add':resultmatrix }
		return render(request,"clustering_popup.html",context)
	elif(algoType == "Mini Batch K-Means"):
		resultcalculation, resultmatrix = calculate_mbkmeans(list_table,pdColumnResult,1)
		accuracyResult = pd.DataFrame()
		resultColumn = resultcalculation.columns.values.tolist()
		resultColumn = pd.DataFrame (resultColumn, columns = ['column_name'])
		accuracyColumn = accuracyResult.columns.values.tolist()
		accuracyColumn = pd.DataFrame (accuracyColumn, columns = ['column_name'])
		context = {"username":username, 'Algo':algoType,'result':resultcalculation, 'accuracy':accuracyResult, 'resultColumn':resultColumn, 'accuracyColumn':accuracyColumn, 'add':resultmatrix }
		return render(request,"clustering_popup.html",context)
	elif(algoType == "Agglomerative"):
		resultcalculation, resultmatrix = calculate_agglomerative(list_table,pdColumnResult,1)
		accuracyResult = pd.DataFrame()
		resultColumn = resultcalculation.columns.values.tolist()
		resultColumn = pd.DataFrame (resultColumn, columns = ['column_name'])
		accuracyColumn = accuracyResult.columns.values.tolist()
		accuracyColumn = pd.DataFrame (accuracyColumn, columns = ['column_name'])
		context = {"username":username, 'Algo':algoType,'result':resultcalculation, 'accuracy':accuracyResult, 'resultColumn':resultColumn, 'accuracyColumn':accuracyColumn, 'add':resultmatrix }
		return render(request,"clustering_popup.html",context)
	elif(algoType == "Spectral"):
		resultcalculation, resultmatrix = calculate_spectral(list_table,pdColumnResult,1)
		accuracyResult = pd.DataFrame()
		resultColumn = resultcalculation.columns.values.tolist()
		resultColumn = pd.DataFrame (resultColumn, columns = ['column_name'])
		accuracyColumn = accuracyResult.columns.values.tolist()
		accuracyColumn = pd.DataFrame (accuracyColumn, columns = ['column_name'])
		context = {"username":username, 'Algo':algoType,'result':resultcalculation, 'accuracy':accuracyResult, 'resultColumn':resultColumn, 'accuracyColumn':accuracyColumn, 'add':resultmatrix }
		return render(request,"clustering_popup.html",context)
	elif(algoType == "BIRCH"):
		resultcalculation, resultmatrix = birch_cluster(list_table,pdColumnResult,1)
		accuracyResult = pd.DataFrame()
		resultColumn = resultcalculation.columns.values.tolist()
		resultColumn = pd.DataFrame (resultColumn, columns = ['column_name'])
		accuracyColumn = accuracyResult.columns.values.tolist()
		accuracyColumn = pd.DataFrame (accuracyColumn, columns = ['column_name'])
		context = {"username":username, 'Algo':algoType,'result':resultcalculation, 'accuracy':accuracyResult, 'resultColumn':resultColumn, 'accuracyColumn':accuracyColumn, 'add':resultmatrix }
		return render(request,"clustering_popup.html",context)
	elif(algoType == "DBSCAN"):
		resultcalculation, resultmatrix = dbscan_cluster(list_table,pdColumnResult,1)
		accuracyResult = pd.DataFrame()
		resultColumn = resultcalculation.columns.values.tolist()
		resultColumn = pd.DataFrame (resultColumn, columns = ['column_name'])
		accuracyColumn = accuracyResult.columns.values.tolist()
		accuracyColumn = pd.DataFrame (accuracyColumn, columns = ['column_name'])
		context = {"username":username, 'Algo':algoType,'result':resultcalculation, 'accuracy':accuracyResult, 'resultColumn':resultColumn, 'accuracyColumn':accuracyColumn, 'add':resultmatrix }
		return render(request,"clustering_popup.html",context)
	elif(algoType == "Trend"):
		#resultcalculation = list_table #to be changed
		resultcalculation, resultmatrix = see_trend(list_table,pdColumnResult,1)

		resultColumn = resultcalculation.columns.values.tolist()
		resultColumn = pd.DataFrame (listColumnResult, columns = ['column_name'])
		context = {"username":username, 'Algo':algoType,'result':resultcalculation, 'accuracy':accuracyResult, 'resultColumn':resultColumn, 'accuracyColumn':accuracyColumn, 'add':resultmatrix }
		return render(request,"trend.html",context)

	# context = {"username":username, 'result':resultcalculation, 'columnName':columnList, 'columnResultName':pdColumnResult } #kalau mau munculin data yg di upload
	context = {"username":username, 'Algo':algoType,'result':resultcalculation, 'accuracy':accuracyResult, 'resultColumn':resultColumn, 'accuracyColumn':accuracyColumn, 'add':resultmatrix }
	return render(request,"",context)

def regression_classification(request, *args, **kwargs):
	username = constructor(request);
	#list_user = AuthUser.objects.all()
	list_user = AuthUser.objects.raw("select * from auth_user where username='ndok'")
	context = {"username":username, 'list_user':list_user}
	return render(request,'regression_classification.html',context)

def convert_ascii_code(a):
	strr=[ord(x) for x in a] if not pd.isnull(a) else []
	b=[]
	for x in strr:
		b.append('{:03}'.format(x)) #Add leading zero, ensuring 3 digits
	b=''.join([ "%s"%x for x in b])
	return int(b) if not pd.isnull(a) else np.nan

@csrf_protect
def TriggerNewChat(request):
	username = constructor(request);
	body_unicode = request.body.decode('utf-8')
	received_json = json.loads(body_unicode)
	parentCode = received_json["parentCode"]
	data = list(Chatlist.objects.filter(parentchatcode=parentCode,issample=0,status=1).values('chatlistcode','parentchatcode','description','isquestion','isreset','isupload','order','mltype').order_by('order'))
	
	json_response = {"ChatData":data}
	return HttpResponse(escape(json.dumps(json_response)))

# @csrf_protect
# def TriggerNewChat(request):
# 	username = constructor(request);
# 	body_unicode = request.body.decode('utf-8')
# 	received_json = json.loads(body_unicode)
# 	parentCode = received_json["parentCode"]
# 	data = list(Chatlist.objects.filter(parentchatcode=parentCode,issample=0,status=1).values('chatlistcode','parentchatcode','description','isquestion','isreset','isupload','order','mltype').order_by('order'))
# 	template = loader.get_template('chat_data.html')
# 	context = {'data':data}
# 	return HttpResponse(template.render(context))

@csrf_protect
def getSampleDescription(request):
	username = constructor(request);
	body_unicode = request.body.decode('utf-8')
	received_json = json.loads(body_unicode)
	parentCode = received_json["chatcode"]
	mltype = received_json["mltype"]
	data = list(Chatlist.objects.filter(parentchatcode=parentCode,mltype=mltype,issample=1,status=1).values('chatlistcode','parentchatcode','description','isquestion','isreset','isupload','order','mltype').order_by('order'))
	
	json_response = {"ChatData":data}	
	return HttpResponse(escape(json.dumps(json_response)))

@csrf_protect
def viewSampleData(request):
	username = constructor(request);
	body_unicode = request.body.decode('utf-8')
	received_json = json.loads(body_unicode)
	mltype = received_json["mltype"]

	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	if(mltype == "Cluster" or mltype == "Trend"):
		filename = 'Clustering_Sample.xlsx'
	elif(mltype == "Probability"):
		filename = 'Classification_Sample.xlsx'
	elif(mltype == "Regression"):
		filename = 'Regression_Sample.xlsx'
	filepath = BASE_DIR + '/static/files/' + filename
	df = pd.read_excel(filepath)
	df = df.head().to_html(index=False,classes=["table"],table_id='clusterTable',escape=False).replace('border="1"','border="0"').replace('<tr style="text-align: right;">', '<tr style="text-align: center;">')
	json_response = {"table":df}
	return JsonResponse(json_response)


@csrf_protect
def validate_file(request):
	username = constructor(request);
	data = request.FILES.get('file')
	mltype = request.POST['mltype']
	list_table = pd.DataFrame();
	df = pd.DataFrame()
	filename = str(data)
	if(filename.endswith((".xlsx", ".xls"))):
		df = pd.read_excel(data)
	elif(filename.endswith((".csv"))):
		df = pd.read_csv(data,delimiter="|")
	else:
		context = {"username":username, "status":'error', "message":'The accepted file type is only xls, xlsx and csv' }
		return HttpResponse(escape(json.dumps(context)))
	list_table = df
		# print(df)

	#input validation
	status = ''
	message = ''
	min_historical = 0
	if(mltype == "Regression"):
		no_null = list_table.iloc[:,0].isnull().sum()
		no_string = list_table.shape[1]-1 #total columns of X and y variables (drop 'value type' columns)
		no_string2 = list_table.select_dtypes(include=['int64','float64']).shape[1] # choosing int & float
		no_typo = list_table.iloc[:,0]
		no_typo2 = list_table.loc[list_table.iloc[:,0].str.lower().isin([x.lower() for x in ['Historical','Predicted']]) ]
		min_historical = len(list_table.loc[list_table.iloc[:,0].str.lower().isin([x.lower() for x in ['Historical']]) ])
	elif(mltype == "Probability"):
		no_null = list_table.iloc[:,0].isnull().sum()
		no_string = list_table.shape[1]-2 #total columns of independent variables (drop 'value type' and 'y' columns)
		no_string2 = list_table.select_dtypes(include=['int64','float64']).shape[1] # choosing int & float
		no_typo = list_table.iloc[:,0]
		no_typo2 = list_table.loc[list_table.iloc[:,0].str.lower().isin([x.lower() for x in ['Historical','Predicted']]) ]
	elif(mltype == "Cluster"):
		no_null = 0
		no_string = list_table.shape[1]
		no_string2 = list_table.select_dtypes(include=['int64','float64']).shape[1] # choosing int & float
		no_typo = list_table.iloc[:,0]
		no_typo2 = list_table.iloc[:,0]
	elif(mltype == "Trend"):
		no_null = 0
		no_string = list_table.shape[1] #total columns of X and y variables (drop 'value type' columns)
		no_string2 = list_table.select_dtypes(include=['int64','float64']).shape[1] # choosing int & float
		no_typo = list_table.iloc[:,0]
		no_typo2 = list_table.iloc[:,0]
		# no_typo2 = list_table.loc[list_table.iloc[:,0].str.lower().isin([x.lower() for x in ['Historical','Predicted']]) ]

	context={}
	if no_null > 0:
		status = 'error'
		message = 'The first column can not contain null value'
		# context={"username":username, "status": status, "message": message }
	elif not len(no_typo) == len(no_typo2):
		status = 'error'
		message = 'Make sure there is no typo in the first column (The first column can only contain "historical" or "predicted" value)'
		# context={"username":username, "status": status, "message": message }
	elif not no_string == no_string2:
		status = 'error'
		if(mltype == "Regression"):
			message = 'Make sure there is only numerical value in the independent & dependent variables'
		elif not no_string < no_string2:
			message = 'Make sure there is only numerical value in the independent variables'
		else:
			status='success'
		# context={"username":username, "status": status, "message": message }
	elif (min_historical < 12 and mltype == "Regression"):
		status = 'error'
		message = 'Need more historical data (The minimum historical data required is 12)'
		# context={"username":username, "status": status, "message": message }
	else:
		status = 'success'
	context = {"username":username, "status":status, "message":message }

	return HttpResponse(escape(json.dumps(context)))

@csrf_protect
def upload_file(request):
	username = constructor(request);
	data = request.FILES.get('file')
	mltype = request.POST['mltype']
	issample = request.POST['issample']
	list_table = pd.DataFrame();
	df = pd.DataFrame()
	if issample=="1":
		BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		if(mltype == "Cluster" or mltype == "Trend"):
			filename = 'Clustering_Sample.xlsx'
		elif(mltype == "Probability"):
			filename = 'Classification_Sample.xlsx'
		elif(mltype == "Regression"):
			filename = 'Regression_Sample.xlsx'
		filepath = BASE_DIR + '/static/files/' + filename
		df = pd.read_excel(filepath)
	else:
		filename = str(data)
		if(filename.endswith(".xlsx") or filename.endswith(".xls")):
			df = pd.read_excel(data)
		else:
			df = pd.read_csv(data,delimiter="|")
	list_table = df
	# print(df)

	# #input validation
	# htmlPage=''
	# status = ''
	# message = ''
	# min_historical = 0
	# if(mltype == "Regression"):
	# 	no_null = list_table.iloc[:,0].isnull().sum()
	# 	no_string = list_table.shape[1]-1 #total columns of X and y variables (drop 'value type' columns)
	# 	no_string2 = list_table.select_dtypes(include=['int64','float64']).shape[1] # choosing int & float
	# 	no_typo = list_table.iloc[:,0]
	# 	no_typo2 = list_table.loc[list_table.iloc[:,0].str.lower().isin([x.lower() for x in ['Historical','Predicted']]) ]
	# 	min_historical = len(list_table.loc[list_table.iloc[:,0].str.lower().isin([x.lower() for x in ['Historical']]) ])
	# elif(mltype == "Probability"):
	# 	no_null = list_table.iloc[:,0].isnull().sum()
	# 	no_string = list_table.shape[1]-2 #total columns of independent variables (drop 'value type' and 'y' columns)
	# 	no_string2 = list_table.select_dtypes(include=['int64','float64']).shape[1] # choosing int & float
	# 	no_typo = list_table.iloc[:,0]
	# 	no_typo2 = list_table.loc[list_table.iloc[:,0].str.lower().isin([x.lower() for x in ['Historical','Predicted']]) ]
	# elif(mltype == "Cluster"):
	# 	no_null = 0
	# 	no_string = list_table.shape[1]
	# 	no_string2 = list_table.select_dtypes(include=['int64','float64']).shape[1] # choosing int & float
	# 	no_typo = list_table.iloc[:,0]
	# 	no_typo2 = list_table.iloc[:,0]
	# elif(mltype == "Trend"):
	# 	no_null = 0
	# 	no_string = list_table.shape[1] #total columns of X and y variables (drop 'value type' columns)
	# 	no_string2 = list_table.select_dtypes(include=['int64','float64']).shape[1] # choosing int & float
	# 	no_typo = list_table.iloc[:,0]
	# 	no_typo2 = list_table.iloc[:,0]
	# 	# no_typo2 = list_table.loc[list_table.iloc[:,0].str.lower().isin([x.lower() for x in ['Historical','Predicted']]) ]

	# context={}
	# if no_null > 0:
	# 	status = 'error'
	# 	message = 'The first column can not contain null value'
	# 	context={"username":username, "status": status, "message": message }
	# elif not len(no_typo) == len(no_typo2):
	# 	status = 'error'
	# 	message = 'Make sure there is no typo in the first column (The first column can only contain "historical" or "predicted" value)'
	# 	context={"username":username, "status": status, "message": message }
	# elif not no_string == no_string2:
	# 	status = 'error'
	# 	if(mltype == "Regression"):
	# 		message = 'Make sure there is only numerical value in the independent & dependent variables'
	# 	else:
	# 		message = 'Make sure there is only numerical value in the independent variables'
	# 	context={"username":username, "status": status, "message": message }
	# elif (min_historical < 12 and mltype == "Regression"):
	# 	status = 'error'
	# 	message = 'Need more historical data (The minimum historical data required is 12)'
	# 	context={"username":username, "status": status, "message": message }
	# else:
	# status = 'success'
	#set a column that ends with a null as the y variable
	y_var=list_table.loc[:, list_table.iloc[-1].isna()]
	#union y column with previous dataset to set y as the first column
	list_table= pd.concat([y_var,list_table], axis=1)
	#drop duplicate y column
	list_table = list_table.loc[:,~list_table.columns.duplicated()]

	column_length = list_table.shape[1]
	if(mltype == "Regression"):
		if list_table.shape[1]>5:
				list_table.drop(list_table.iloc[:,5:list_table.shape[1]], axis=1, inplace=True)
		list_table.iloc[:,2:column_length] = list_table.iloc[:,2:column_length].fillna(method='ffill')
	elif(mltype == "Probability"):
		if list_table.shape[1]>5:
				list_table.drop(list_table.iloc[:,5:list_table.shape[1]], axis=1, inplace=True)	
		list_table.iloc[:,2:column_length] = list_table.iloc[:,2:column_length].fillna(method='ffill')		
	elif(mltype == "Cluster"):
		if list_table.shape[1]>3:
				list_table.drop(list_table.iloc[:,3:list_table.shape[1]], axis=1, inplace=True)
		list_table.iloc[:,0:column_length] = list_table.iloc[:,0:column_length].fillna(method='ffill')
	elif(mltype == "Trend"):
		if list_table.shape[1]>5:
				list_table.drop(list_table.iloc[:,5:list_table.shape[1]], axis=1, inplace=True)	
		list_table.iloc[:,0:column_length] = list_table.iloc[:,0:column_length].fillna(method='ffill')

	column_length = list_table.shape[1]
	listOriginalColumn = list_table.columns.values.tolist()
	columnList = pd.DataFrame (listOriginalColumn, columns = ['column_name'])
	
	for i in range(column_length):
		list_table = list_table.rename(columns={ list_table.columns[i]: "value"+str(i+1) })

	resultcalculation = pd.DataFrame();
	listColumnResult = list_table.columns.values.tolist()
	pdColumnResult = pd.DataFrame (listOriginalColumn, columns = ['column_name'])
	if(mltype == "Regression"):
		list_table['value2'] = list_table['value2'].str.title()
		regressionresult = pd.DataFrame();
		regressionresult, resultmatrix = calculate_linear_regression(list_table,pdColumnResult)
		
		regressionresult['Visualisation'] = format_html('<img src="data:image/png;base64, {}" width="250px">', resultmatrix)
		regressionresult['Action'] = format_html('<div class="viewMore" AlgoType="Linear Regression" style="color:black;text-align-last:left;width:max-content;background-color:#d93954 !important;"><a>View more</a></div>')
		regressionresult = regressionresult[['Algorithm', 'Visualisation', 'RMSE', 'MAPE', 'AdjRSQ','Action']]
		resultcalculation = regressionresult

		arimaresult = pd.DataFrame();
		resultmatrix = ''
		arimaresult, resultmatrix = calculate_arima(list_table,pdColumnResult)
		arimaresult['Visualisation'] = format_html('<img src="data:image/png;base64, {}" width="250px">', resultmatrix)
		arimaresult['Action'] = format_html('<div class="viewMore" AlgoType="ARIMA" style="color:black;text-align-last:left;width:max-content;background-color:#d93954 !important;"><a>View more</a></div>')
		arimaresult = arimaresult[['Algorithm', 'Visualisation', 'RMSE', 'MAPE', 'AdjRSQ','Action']]
		resultcalculation = resultcalculation.append(arimaresult)

		log_reg = pd.DataFrame();
		resultmatrix = ''
		log_reg, resultmatrix = calculate_polynomial_regression(list_table,pdColumnResult)
		log_reg['Visualisation'] = format_html('<img src="data:image/png;base64, {}" width="250px">', resultmatrix)
		log_reg['Action'] = format_html('<div class="viewMore" AlgoType="Polynomial Regression" style="color:black;text-align-last:left;width:max-content;background-color:#d93954 !important;"><a>View more</a></div>')
		log_reg = log_reg[['Algorithm', 'Visualisation', 'RMSE', 'MAPE', 'AdjRSQ','Action']]
		resultcalculation = resultcalculation.append(log_reg)

		svr = pd.DataFrame();
		resultmatrix = ''
		svr, resultmatrix = calculate_svr(list_table,pdColumnResult)
		svr['Visualisation'] = format_html('<img src="data:image/png;base64, {}" width="250px">', resultmatrix)
		svr['Action'] = format_html('<div class="viewMore" AlgoType="Support Vector Machines Regression" style="color:black;text-align-last:left;width:max-content;background-color:#d93954 !important;"><a>View more</a></div>')
		svr = svr[['Algorithm', 'Visualisation', 'RMSE', 'MAPE', 'AdjRSQ','Action']]
		resultcalculation = resultcalculation.append(svr)

		knn_regres = pd.DataFrame();
		resultmatrix = ''
		knn_regres, resultmatrix = calculate_knnregr(list_table,pdColumnResult)
		knn_regres['Visualisation'] = format_html('<img src="data:image/png;base64, {}" width="250px">', resultmatrix)
		knn_regres['Action'] = format_html('<div class="viewMore" AlgoType="K-nearest Neighbour Regression" style="color:black;text-align-last:left;width:max-content;background-color:#d93954 !important;"><a>View more</a></div>')
		knn_regres = knn_regres[['Algorithm', 'Visualisation', 'RMSE', 'MAPE', 'AdjRSQ','Action']]
		resultcalculation = resultcalculation.append(knn_regres)

		random_forest = pd.DataFrame();
		resultmatrix = ''
		random_forest, resultmatrix = rf_regression(list_table,pdColumnResult)
		random_forest['Visualisation'] = format_html('<img src="data:image/png;base64, {}" width="250px">', resultmatrix)
		random_forest['Action'] = format_html('<div class="viewMore" AlgoType="Random Forest Regression" style="color:black;text-align-last:left;width:max-content;background-color:#d93954 !important;"><a>View more</a></div>')
		random_forest = random_forest[['Algorithm', 'Visualisation', 'RMSE', 'MAPE', 'AdjRSQ','Action']]
		resultcalculation = resultcalculation.append(random_forest)

		dec_tree_reg = pd.DataFrame();
		resultmatrix = ''
		dec_tree_reg, resultmatrix = calculate_dectree_regress(list_table,pdColumnResult)
		dec_tree_reg['Visualisation'] = format_html('<img src="data:image/png;base64, {}" width="250px">', resultmatrix)
		dec_tree_reg['Action'] = format_html('<div class="viewMore" AlgoType="Decision Tree Regression" style="color:black;text-align-last:left;width:max-content;background-color:#d93954 !important;"><a>View more</a></div>')
		dec_tree_reg = dec_tree_reg[['Algorithm', 'Visualisation', 'RMSE', 'MAPE', 'AdjRSQ','Action']]
		resultcalculation = resultcalculation.append(dec_tree_reg)

		#column name follow from uploaded data
		listColumnResult = resultcalculation.columns.values.tolist()
		# resultcalculation = resultcalculation.to_html(index=False,classes=["table"],table_id='regressionTable',escape=False)


		pdColumnResult = pd.DataFrame (listColumnResult, columns = ['column_name'])
		context = {"username":username, 'result':resultcalculation, 'columnResultName':pdColumnResult, 'add':resultmatrix }
		return render(request,"regression.html",context)
	elif(mltype == "Probability"):
		list_table['value2'] = list_table['value2'].str.title()
		knnresult = calculate_knnclas(list_table,pdColumnResult)
		resultmatrix = ''
		knnresult['Action'] = format_html('<div class="viewMore" AlgoType="K-nearest Neighbour Class" style="color:black;text-align-last:left;width:max-content;background-color:#d93954 !important;"><a>View more</a></div>')
		
		resultcalculation = knnresult

		dectreeresult = calculate_dectree(list_table,pdColumnResult)
		resultmatrix = ''
		dectreeresult['Action'] = format_html('<div class="viewMore" AlgoType="Decision Tree" style="color:black;text-align-last:left;width:max-content;background-color:#d93954 !important;"><a>View more</a></div>')
		
		resultcalculation = resultcalculation.append(dectreeresult)

		log_reg_result = calculate_logistic_regression_classification(list_table,pdColumnResult)
		resultmatrix = ''
		log_reg_result['Action'] = format_html('<div class="viewMore" AlgoType="Logistic Regression Classification" style="color:black;text-align-last:left;width:max-content;background-color:#d93954 !important;"><a>View more</a></div>')
		resultcalculation = resultcalculation.append(log_reg_result)

		random_forest_clas = rf_class(list_table,pdColumnResult)
		resultmatrix = ''
		random_forest_clas['Action'] = format_html('<div class="viewMore" AlgoType="Random Forest Classification" style="color:black;text-align-last:left;width:max-content;background-color:#d93954 !important;"><a>View more</a></div>')
		resultcalculation = resultcalculation.append(random_forest_clas)

		svm_clas = calculate_svm(list_table,pdColumnResult)
		resultmatrix = ''
		svm_clas['Action'] = format_html('<div class="viewMore" AlgoType="Support Vector Machines Classification" style="color:black;text-align-last:left;width:max-content;background-color:#d93954 !important;"><a>View more</a></div>')
		resultcalculation = resultcalculation.append(svm_clas)

		listColumnResult = resultcalculation.columns.values.tolist()
		pdColumnResult = pd.DataFrame (listColumnResult, columns = ['column_name'])
		context = {"username":username, 'result':resultcalculation, 'columnResultName':pdColumnResult, 'add':resultmatrix }
		return render(request,"probability.html",context)
	elif(mltype == "Cluster"):
		kmeansresult, resultmatrix = calculate_kmeans(list_table,pdColumnResult)
		kmeansresult['Visualisation'] = format_html('<img src="data:image/png;base64, {}" width="250px">', resultmatrix)
		kmeansresult['Action'] = format_html('<div class="viewMore" AlgoType="K-Means" style="color:black;text-align-last:left;width:max-content;background-color:#d93954 !important;"><a>View more</a></div>')
		kmeansresult = kmeansresult[['Algorithm', 'Visualisation','Action']]
		resultcalculation = kmeansresult

		mbkmeansresult, resultmatrix = calculate_mbkmeans(list_table,pdColumnResult)
		mbkmeansresult['Visualisation'] = format_html('<img src="data:image/png;base64, {}" width="250px">', resultmatrix)
		mbkmeansresult['Action'] = format_html('<div class="viewMore" AlgoType="Mini Batch K-Means" style="color:black;text-align-last:left;width:max-content;background-color:#d93954 !important;"><a>View more</a></div>')
		mbkmeansresult = mbkmeansresult[['Algorithm', 'Visualisation','Action']]
		resultcalculation = resultcalculation.append(mbkmeansresult)

		agglo, resultmatrix = calculate_agglomerative(list_table,pdColumnResult)
		agglo['Visualisation'] = format_html('<img src="data:image/png;base64, {}" width="250px">', resultmatrix)
		agglo['Action'] = format_html('<div class="viewMore" AlgoType="Agglomerative" style="color:black;text-align-last:left;width:max-content;background-color:#d93954 !important;"><a>View more</a></div>')
		agglo = agglo[['Algorithm', 'Visualisation','Action']]
		resultcalculation = resultcalculation.append(agglo)

		spectralresult, resultmatrix = calculate_spectral(list_table,pdColumnResult)
		spectralresult['Visualisation'] = format_html('<img src="data:image/png;base64, {}" width="250px">', resultmatrix)
		spectralresult['Action'] = format_html('<div class="viewMore" AlgoType="Spectral" style="color:black;text-align-last:left;width:max-content;background-color:#d93954 !important;"><a>View more</a></div>')
		spectralresult = spectralresult[['Algorithm', 'Visualisation','Action']]
		resultcalculation = resultcalculation.append(spectralresult)

		birchresult, resultmatrix = birch_cluster(list_table,pdColumnResult)
		birchresult['Visualisation'] = format_html('<img src="data:image/png;base64, {}" width="250px">', resultmatrix)
		birchresult['Action'] = format_html('<div class="viewMore" AlgoType="BIRCH" style="color:black;text-align-last:left;width:max-content;background-color:#d93954 !important;"><a>View more</a></div>')
		birchresult = birchresult[['Algorithm', 'Visualisation','Action']]
		resultcalculation = resultcalculation.append(birchresult)

		dbscanresult, resultmatrix = dbscan_cluster(list_table,pdColumnResult)
		dbscanresult['Visualisation'] = format_html('<img src="data:image/png;base64, {}" width="250px">', resultmatrix)
		dbscanresult['Action'] = format_html('<div class="viewMore" AlgoType="DBSCAN" style="color:black;text-align-last:left;width:max-content;background-color:#d93954 !important;"><a>View more</a></div>')
		dbscanresult = dbscanresult[['Algorithm', 'Visualisation','Action']]
		resultcalculation = resultcalculation.append(dbscanresult)
		
		listColumnResult = resultcalculation.columns.values.tolist()
		# resultcalculation = resultcalculation.to_html(index=False,classes=["table"],table_id='clusterTable',escape=False)

		pdColumnResult = pd.DataFrame (listColumnResult, columns = ['column_name'])
		context = {"username":username, 'result':resultcalculation, 'columnResultName':pdColumnResult, 'add':resultmatrix }
		print(context)
		return render(request,"cluster.html",context)
	elif(mltype == "Trend"):
		# list_table['value2'] = list_table['value2'].str.title()
		# trend = pd.DataFrame();
		resultmatrix = ''
		linetrend, resultmatrix = line_trend(list_table,pdColumnResult)
		linetrend['Visualisation'] = format_html('<img src="data:image/png;base64, {}" height="200px">', resultmatrix)
		# trend['Action'] = '<div class="viewMore" AlgoType="Line" style="color:black;text-align-last:left;width:max-content;background-color:#d93954 !important;"><a>View more</a></div>'
		resultcalculation = linetrend
		
		bartrend, resultmatrix = bar_trend(list_table,pdColumnResult)
		bartrend['Visualisation'] = format_html('<img src="data:image/png;base64, {}" height="200px">', resultmatrix)
		resultcalculation = resultcalculation.append(bartrend)

		scattertrend, resultmatrix = scatter_trend(list_table,pdColumnResult)
		scattertrend['Visualisation'] = format_html('<img src="data:image/png;base64, {}" height="200px">', resultmatrix)
		resultcalculation = resultcalculation.append(scattertrend)

		histtrend, resultmatrix = hist_trend(list_table,pdColumnResult)
		histtrend['Visualisation'] = format_html('<img src="data:image/png;base64, {}" height="200px">', resultmatrix)
		resultcalculation = resultcalculation.append(histtrend)

		statinarytrend, resultmatrix = stat_trend(list_table,pdColumnResult)
		statinarytrend['Visualisation'] = format_html('<img src="data:image/png;base64, {}" height="200px">', resultmatrix)
		resultcalculation = resultcalculation.append(statinarytrend)

		listColumnResult = resultcalculation.columns.values.tolist()
		# resultcalculation = resultcalculation.to_html(index=False,classes=["table"],table_id='trendTable',escape=False)
		pdColumnResult = pd.DataFrame (listColumnResult, columns = ['column_name'])
		context = {"username":username, 'result':resultcalculation, 'columnResultName':pdColumnResult, 'add':resultmatrix }
		return render(request,"trend.html",context)

	context = {"username":username, 'result':resultcalculation, 'columnResultName':pdColumnResult, 'add':resultmatrix }

	# if status == 'success':
	return render(request,'',context)
	# else:
		# return JsonResponse (context)