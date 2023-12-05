#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import all libraries
import pandas as pd #data anlaysis
import numpy as np #perform scientific calculation
#% matplotlib inline
import math #basic mathematical function

# Import graphical libraries
import matplotlib.pyplot as plt
import seaborn as sns

#import machine learning libraries
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

#import other libraries for integration
import os
import sys
import matplotlib.pyplot as plt
from io import BytesIO
import time
import base64

#TEMPORARY BUAT TEST DI JUPYTERLAB MATIIN***********************************************************************************
current_directory = sys.path[0]
current_directory = os.path.dirname(current_directory)
final_directory = os.path.join(current_directory, r'log')
if not os.path.exists(final_directory):
    os.makedirs(final_directory)
#TEMPORARY BUAT TEST DI JUPYTERLAB MATIIN***********************************************************************************


#TEMPORARY BUAT TEST DI JUPYTERLAB NYALAIN**********************************************************************************
#final_directory = r"C:\Users\Firsta Kamandika\Documents\Research 2022\Logistic Regression\Data\datasets-master\IRIS.csv"
#data = pd.read_csv(final_directory,index_col=False, sep = "|")
#lendata = len(data)
#paramColumn = list(data.columns.values)
#paramColumn

#paramdf = data
#paramdf.columns = [''] * len(paramdf.columns)
#paramdf.head(n=2)
#TEMPORARY BUAT TEST DI JUPYTERLAB NYALAIN**********************************************************************************


def calculate_logistic_regression(paramdf, paramColumn, viewParam=0):
    start = time.time()
    x_data = paramdf
    
    datainput = paramdf
    datainput.columns = paramColumn
    #datainput.head(n=2)
    
    historicaldata = datainput.dropna()
    counthistoricaldata = len(historicaldata)
    #print(counthistoricaldata)
    #historicaldata.head(n=3) 

    projecteddata = datainput[counthistoricaldata:]
    #print(len(projecteddata))
    projecteddata = projecteddata.drop(projecteddata.columns[0], axis = 1) 
    #projecteddata.head(n=3) #read data
    
    firstcolumnhistoricaldata = historicaldata.iloc[:,0]
    #firstcolumnhistoricaldata.head(n=3)
    
    secondtolastcolumnhistoricaldata = historicaldata[historicaldata.columns[1:]]
    #secondtolastcolumnhistoricaldata.head(n=3)
    
    X= secondtolastcolumnhistoricaldata #idendependt varibale, drop the survive only
    y= firstcolumnhistoricaldata #output value that we need to predict, are passangers survived or not
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=1) #testnya 30 train 70
    
    #Train the model
    model = LogisticRegression(fit_intercept = False, C = 1e9)
    model.fit(X_train, y_train) #Training the model
    
    colname = data.columns[0]
    #print (colname)
    
    predictions = model.predict(X_test) #prediciton value nya X test
    X_test['lastcolumn'] = predictions
    X_test.columns = [*X_test.columns[:-1], colname]
    X_test.head(n=5)
    
    modelcoefficient = model.coef_
    
    otherdatasetpredictions = model.predict(projecteddata) #prediciton value nya X test
    projecteddata['lastcolumn'] = otherdatasetpredictions
    projecteddata.columns = [*projecteddata.columns[:-1], colname]
    #projecteddata

    temp_cols=projecteddata.columns.tolist()
    new_cols=temp_cols[-1:] + temp_cols[:-1]
    projecteddata=projecteddata[new_cols]
    #projecteddata.head(n=3)
    
    datafinalmerged = pd.concat([historicaldata, projecteddata], ignore_index=True)
    
    historicaldata['datatype'] = 'Historical'
    projecteddata['datatype'] = 'Predicted'

    datafinalmerged2 = pd.concat([historicaldata, projecteddata], ignore_index=True)
    #datafinalmerged
    
    temp_cols=datafinalmerged2.columns.tolist()
    new_cols=temp_cols[-1:] + temp_cols[:-1]
    datafinalmerged2=datafinalmerged2[new_cols]
    
    def createList(n):
        lst = []
        for i in range(n+1):
            lst.append(i)
        return(lst)

    x = createList(lendata)
    x.pop(0)
    #print(x)

    classificationreport = classification_report(y_test, predictions, output_dict=True) #dikeluarin as dict supaya bisa disave ke df
    #print(classificationreport)
    classificationreportdf = pd.DataFrame(classificationreport).transpose()
    #classificationreportdf
    
    y = datafinalmerged.iloc[:,0]

    import matplotlib.pyplot as plt
    plt.xlabel('Number of Data')
    plt.ylabel('Prediction')

    plt.scatter(x[:counthistoricaldata], y[:counthistoricaldata], color = 'g', marker = '*', s=100, label = 'Historical Data') #alpha=0.6
    plt.scatter(x[counthistoricaldata:],y[counthistoricaldata:], color = 'r', marker = '*', s=100, label = 'Prediction Data') #alpha=0.6

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    plt.legend()
    plt.grid()

    #plt.clf()
    #plt.cla()
    #plt.close()

    plt = base64.b64encode(image_png)
    plt = plt.decode('utf-8')
    
    end = time.time()
    a={"Time":end-start}
    # print(a)
    
    if(viewParam==0):
        return classificationreportdf, datafinalmerged2
    else:
        return datafinalmerged, classificationreportdf, plt


# In[ ]:




