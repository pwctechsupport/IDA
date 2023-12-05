#!/usr/bin/env python
# coding: utf-8

# In[11]:


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

current_directory = sys.path[0]
current_directory = os.path.dirname(current_directory)
final_directory = os.path.join(current_directory, r'\Firsta Kamandika\Documents\Research 2022\Logistic Regression\Data\datasets-master\IRIS.csv')
if not os.path.exists(final_directory):
    os.makedirs(final_directory)

#print(final_directory)

#TEMPORARY BUAT TEST DI JUPYTERLAB
#final_directory = r"C:\Users\Firsta Kamandika\Documents\Research 2022\Logistic Regression\Data\datasets-master\ilustrasi_dataset_klasifikasi.csv"
#final_directory = r"C:\Users\Firsta Kamandika\Documents\Research 2022\Logistic Regression\Data\datasets-master\IRIS.csv"
#data = pd.read_csv(final_directory,index_col=False, sep = "|")
#lendata = len(data)
#print(lendata)
#data.head(n=5) #read data


# In[12]:


#TEMPORARY BUAT TEST DI JUPYTERLAB
#paramColumn = list(data.columns.values)
#paramColumn


# In[13]:


#TEMPORARY BUAT TEST DI JUPYTERLAB
#kolomnyadoko = ["value1", "value2", "value3", "value4", "value5", "value6"]
#paramdf = data
#paramdf.columns = kolomnyadoko
#paramdf.head(n=2)


# In[16]:


def calculate_logistic_regression_classification(paramdf, paramColumn, viewParam=0):
    start = time.time()
    x_data = paramdf
    datainput = paramdf
    lendata = len(paramdf)
    
    # paramColumn = pd.DataFrame({'column_name':paramColumn})
    
    for i in range(len(paramColumn)):
        datainput = datainput.rename(columns={ datainput.columns[i]: paramColumn['column_name'][i] })
        
    historicaldata = paramdf.loc[paramdf['value2'] == 'Historical']
    counthistoricaldata = len(historicaldata)

    projecteddata = datainput[counthistoricaldata:]
    projecteddata = projecteddata.drop([projecteddata.columns[0],projecteddata.columns[1]], axis = 1) 
    
    firstcolumnhistoricaldata = historicaldata.iloc[:,0]
    secondtolastcolumnhistoricaldata = historicaldata[historicaldata.columns[2:]]
    
    X= secondtolastcolumnhistoricaldata
    y= firstcolumnhistoricaldata
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=42)
    
    #Train the model
    model = LogisticRegression(fit_intercept = False, C = 1e9)
    model.fit(X_train, y_train) #Training the model
    
    colname = datainput.columns[0]
    
    predictions = model.predict(X_test)
    X_test['lastcolumn'] = predictions
    X_test.columns = [*X_test.columns[:-1], colname]
    X_test.head(n=5)
    
    modelcoefficient = model.coef_
    
    otherdatasetpredictions = model.predict(projecteddata)
    projecteddata['lastcolumn'] = otherdatasetpredictions
    
    projecteddata.columns = [*projecteddata.columns[:-1], colname]
    
    temp_cols=projecteddata.columns.tolist()
    
    new_cols=temp_cols[-1:] + temp_cols[:-1]
    
    projecteddata=projecteddata[new_cols]
    
    projecteddata['datatype'] = 'Predicted'
    
    temp_cols=projecteddata.columns.tolist()
    
    pertamasampesebelumakhir = temp_cols[:-1]
    pertamasampesebelumakhir.pop(0)
    new_cols=temp_cols[0:1] + temp_cols[-1:] + pertamasampesebelumakhir
    projecteddata=projecteddata[new_cols]
    
    historicaldata.columns = list(paramColumn.iloc[:,0])
    projecteddata.columns = list(paramColumn.iloc[:,0])
    datafinalmerged2 = pd.concat([historicaldata, projecteddata], ignore_index=True)
    
    temp_cols=datafinalmerged2.columns.tolist()
    new_cols=temp_cols[-1:] + temp_cols[:-1]
    
    def createList(n):
        lst = []
        for i in range(n+1):
            lst.append(i)
        return(lst)

    x = createList(lendata)
    x.pop(0)
    
    accuracy = classification_report(y_test, predictions, output_dict=True) #dikeluarin as dict supaya bisa disave ke df
    
    df_accuracy = pd.DataFrame(accuracy).transpose()
    df_accuracy = df_accuracy.iloc[:-3,:].round(2)
    df_accuracy = df_accuracy.rename(columns={'f1-score': 'f1Score'})
    df_accuracy['Algorithm'] = 'Logistic Regression'
    
    end = time.time()
    a={"Time":end-start}
    
    if(viewParam==0):
        return df_accuracy
    else:
        return df_accuracy, datafinalmerged2


# In[17]:


#calculate_logistic_regression_classification(paramdf, paramColumn)


# In[ ]:





# In[ ]:




