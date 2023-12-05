#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import all libraries
import pandas as pd #data anlaysis
import numpy as np #perform scientific calculation
#% matplotlib inline
import math #basic mathematical function

# Import graphical libraries
import seaborn as sns

#import machine learning libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.metrics import mean_squared_error

#import other libraries for integration
import os
import sys

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
#final_directory = r"C:\Users\Firsta Kamandika\Documents\Research 2022\Logistic Regression\Data\datasets-master\regression_dataset v2.csv"
#data = pd.read_csv(final_directory,index_col=False, sep = "|")
#lendata = len(data)
#print(lendata)
#data.head(n=5) #read data


# In[2]:


#TEMPORARY BUAT TEST DI JUPYTERLAB
#paramColumn = list(data.columns.values)
#paramColumn


# In[3]:


#TEMPORARY BUAT TEST DI JUPYTERLAB
#kolomnyadoko = ["value1", "value2", "value3", "value4"]
#paramdf = data
#paramdf.columns = kolomnyadoko
#paramdf.head(n=2)


# In[4]:


def calculate_polynomial_regression(paramdf, paramColumn, viewParam=0):
    start = time.time()
    x_data = paramdf
    datainput = paramdf
    lendata = len(paramdf)
    
    n = 2
    
    #paramColumn = pd.DataFrame({'column_name':paramColumn}) #nanti dimatiin ya
    
    for i in range(len(paramColumn)):
        datainput = datainput.rename(columns={ datainput.columns[i]: paramColumn['column_name'][i] })
    
    #DEFINE WHICH ONE IS HISTORICAL DATA
    historicaldata = x_data.loc[x_data['value2'] == 'Historical']
    counthistoricaldata = len(historicaldata)
    
    firstcolumnhistoricaldata = historicaldata.iloc[:,0]
    secondtolastcolumnhistoricaldata = historicaldata[historicaldata.columns[2:]]

    #DEFINE WHICH ONE IS PROJECTED DATA
    projecteddata = x_data.loc[x_data['value2'] == 'Predicted']
    projecteddata = projecteddata.drop(projecteddata.columns[0], axis = 1)
    projecteddata = projecteddata.drop(projecteddata.columns[0], axis = 1)
    
    #Split data into a training and a test dataset
    X, y = secondtolastcolumnhistoricaldata, firstcolumnhistoricaldata
    poly = PolynomialFeatures(degree=n, include_bias=False)
    poly_features = poly.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(poly_features, y, test_size=0.3, random_state=42)
    
    #Make model, fit, and predict
    poly_reg_model = LinearRegression()
    poly_reg_model.fit(X_train, y_train)

    poly_reg_y_predicted = poly_reg_model.predict(X_test)

    #RMSE
    poly_reg_rmse = np.sqrt(mean_squared_error(y_test, poly_reg_y_predicted))
    
    #MAPE
    mape= mean_absolute_percentage_error(y_test, poly_reg_y_predicted)
    
    #Poly transform the projected data
    poly = PolynomialFeatures(degree=n, include_bias=False)
    poly_features = poly.fit_transform(projecteddata)
    
    #Predict the projected data
    poly_reg_y_predicted = poly_reg_model.predict(poly_features)
    
    #SECOND TO LAST COLUMN OF WHOLE DATA
    secondtolastcolumndata = x_data[x_data.columns[2:]]
    
    poly = PolynomialFeatures(degree=n, include_bias=False)
    poly_features2 = poly.fit_transform(secondtolastcolumndata)
    poly_reg_y_predicted2 = poly_reg_model.predict(poly_features2)
    
    #Rapihin data
    dfpoly_reg_y_predicted2 = pd.DataFrame(poly_reg_y_predicted2)
    dfpoly_reg_y_predicted2.rename(columns={ dfpoly_reg_y_predicted2.columns[0]: "predictedcolumn" }, inplace = True)

    dfgabungan = pd.concat([x_data, dfpoly_reg_y_predicted2], axis=1)

    # fill missing values
    dfgabungan.iloc[:,0].fillna(dfgabungan.iloc[:,-1], inplace=True)
    dfgabungan = dfgabungan.iloc[:, :-1]
    #dfgabungan.columns = paramColumn
    dfgabungan.columns = list(paramColumn.iloc[:,0]) #ini ntar yg dinyalain instead yg atas pas integrasi doko
    dfgabungan = pd.concat( [dfgabungan.iloc[:,1],dfgabungan.iloc[:,0]], axis=1)
    dfgabungan.rename(columns={dfgabungan.columns[0]: 'Data Type', dfgabungan.columns[1]: 'Value'},inplace=True)
    #DATA PLOT
    ###
    def createList(n):
        lst = []
        for i in range(n+1):
            lst.append(i)
        return(lst)

    xhist = createList(lendata)
    xhist.pop(0)
    ###
    
    ###
    def createList(n):
        lst = []
        for i in range(n+1):
            lst.append(i)
        return(lst)

    x = createList(counthistoricaldata)
    x.pop(0)
    ###
    import matplotlib.pyplot as plt
    # plt.xlabel('Number of Data')
    # plt.ylabel('Prediction')

    plt.plot(xhist[:counthistoricaldata], historicaldata.iloc[:,0], color = 'r', label = 'Historical Data')
    plt.plot(xhist,poly_reg_y_predicted2, color = 'b', label = 'Prediction Data')
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), fancybox=True, shadow=True, ncol=5)
    plt.title('Polynomial Regression Graph')
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    plt.clf()
    plt.cla()
    plt.close()

    plt = base64.b64encode(image_png)
    plt = plt.decode('utf-8')
    
    #REPORTS
    r_squared = poly_reg_model.score(X_train, y_train)
    adjusted_r_squared = 1 - (1-r_squared)*(len(y_train)-1)/(len(y_train)-X_train.shape[1]-1)
    reportdata = [['Polynomial Regression', poly_reg_rmse, mape, adjusted_r_squared]]
    dfreport = pd.DataFrame(reportdata, columns = ['Algorithm', 'RMSE', 'MAPE', 'AdjRSQ'])
    
    end = time.time()
    a={"Time":end-start}
    
    if(viewParam==0):
        return dfreport, plt
    else:
        return dfgabungan, dfreport, plt


# In[5]:


#calculate_polynomial_regression(paramdf, paramColumn)


# In[ ]:




