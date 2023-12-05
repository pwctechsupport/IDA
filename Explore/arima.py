import flask
import itertools
import time
import numpy as np
import statsmodels.api as sm
import statsmodels.stats.api as sms
import scipy.stats as stats
from scipy.stats import shapiro
import pandas as pd
import os
import sys
import logging
import traceback
import warnings
import calendar
import math
import base64
from io import BytesIO
from statsmodels.tsa.arima_model import ARIMA
from scipy.stats import t
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from flask import jsonify
from flask import request
from logging.handlers import RotatingFileHandler
from datetime import datetime
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.libqsturng import psturng

current_directory = sys.path[0]
current_directory = os.path.dirname(current_directory)
final_directory = os.path.join(current_directory, r'log')
if not os.path.exists(final_directory):
   os.makedirs(final_directory)

# evaluate an ARIMA model for a given order (p,d,q) and return RMSE
def evaluate_arima_model(X, arima_order):
    # prepare training dataset
    X = X.astype('float32')
    train_size = int(len(X) * 0.7)
    train, test = X[0:train_size], X[train_size:]
    history = [x for x in train]
    # make predictions
    predictions = list()
    model = ARIMA(history, order=arima_order)
    model_fit = model.fit(trend='nc', disp=0)
    
    yhat = model_fit.forecast(steps=len(test))[0]
    for y in yhat:
        predictions.append(y)
    # calculate out of sample error
    mse = mean_squared_error(test, predictions)
    rmse = math.sqrt(mse)
    train1 = X
    history1 = [x for x in train1]
    try:
        model1 = ARIMA(history1, order=arima_order)
        model_fit1 = model1.fit(trend='nc', disp=0)
        yhat = model_fit1.forecast(steps=len(test))[0]
    except:
        rmse = 999999999999999
    return rmse

# evaluate combinations of p, d and q values for an ARIMA model
def evaluate_models(dataset, p_values, d_values, q_values):
    dataset = dataset.astype('float32')
    best_score, best_cfg = float("inf"), None
    for p in p_values:
        for d in d_values:
            for q in q_values:
                order = (p,d,q)
                try:
                    mse = evaluate_arima_model(dataset, order)
                    if mse < best_score:
                        best_score, best_cfg = mse, order
                except:
                    continue
#    print('Best ARIMA%s MSE=%.3f' % (best_cfg, best_score))
    return best_cfg

def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + int(math.floor(month / 12))
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year,month)[1])
    stringDate = str(year)+"-"+str(month)+"-"+str(day)
    return datetime.strptime(stringDate, '%Y-%m-%d')
    
    
def calculate_arima(paramdf, paramColumn, viewParam=0):
    start = time.time()
    historicalData = paramdf
    x_data = historicalData
    x_data = x_data.loc[x_data['value2'] == 'Historical']
    # print(x_data)
    # evaluate parameters
    p_values = range(1, 2)
    d_values = range(0, 3)
    q_values = range(1, 2)
    warnings.filterwarnings("ignore")
    best_order = evaluate_models(x_data['value1'], p_values, d_values, q_values)
    train = x_data['value1']
    train = train.astype('float32')
    train_size = int(len(train) * 0.7)
    train, test = train[0:train_size], train[train_size:]
    
    for_prediction = paramdf.loc[paramdf['value2'] == 'Predicted']
    lengthPrediction = len(for_prediction);

    lengthData = len(test);
    history = [x for x in train]
    # make predictions
    predictions = list()
    # lastDate = datetime.strptime(series.Period.values[len(train)-1],'%Y-%m-%d')
    # print(best_order)
    model = ARIMA(history, order=best_order)
    # model = ARIMA(history, order=(1,1,1))
    model_fit = model.fit(trend='nc', disp=0)
    #y_test = model_fit.forecast(steps=lengthData)[0]
    y_test = model_fit.forecast(steps=lengthData)[0]
    y_prediction = model_fit.forecast(steps=lengthData+lengthPrediction)[0]

    mse = mean_squared_error(test, y_test)
    rmse = math.sqrt(mse)
    difference_y = (test-y_test)
    mape = np.mean(np.abs(difference_y / test))
    r2 = r2_score(test, y_test)
    Adj_r2 = 1 - (1-r2_score(test, y_test)) * (len(test)-1)/(len(test)-x_data.shape[1]-1)

    list_y_predict = [x for x in y_prediction]
    test = [x for x in test]

    list_y_predict = pd.DataFrame(list_y_predict)
    list_y_predict = list_y_predict[0]
    test = pd.DataFrame(test)
    test = test[0]
    rangeData = range(train_size+1,train_size+lengthData+lengthPrediction+1)
    rangeData2 = range(1,len(x_data['value1'])+1)
    
    import matplotlib.pyplot as plt

    plt.plot(rangeData2, x_data['value1'], "-r", label="Historical Data")
    plt.plot(rangeData,list_y_predict, "-b", label="Prediction Data")
    
    plt.title('ARIMA Graph')
    # plt.xlabel('Number of Data')
    # plt.ylabel('Data comparison')
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),fancybox=True, shadow=True, ncol=5)
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
    returnAccuracy = pd.DataFrame([['ARIMA',rmse,mape,Adj_r2]], columns=['Algorithm','RMSE','MAPE','AdjRSQ'])
    returnData = pd.DataFrame()
    returnData['Value'] = paramdf.dropna(subset=[x_data.columns[0]])['value1']
    returnData['Data Type'] = 'Historical'

    prediction_df = pd.DataFrame()
    prediction_df['Value'] = y_prediction
    prediction_df['Data Type'] = 'Predicted'
    returnData = returnData.append(prediction_df)
    returnData = returnData[['Data Type','Value']]

    end = time.time()
    a=end-start
   
    if(viewParam==0):
         return returnAccuracy, plt
    else:
        return returnData, returnAccuracy, plt
