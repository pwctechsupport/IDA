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
from io import BytesIO

current_directory = sys.path[0]
current_directory = os.path.dirname(current_directory)
final_directory = os.path.join(current_directory, r'log')
if not os.path.exists(final_directory):
   os.makedirs(final_directory)

def calculate_linear_regression(paramdf, paramColumn, viewParam=0):
    start = time.time()
    x_data = paramdf
    x_data = x_data.loc[x_data['value2'] == 'Historical']
    columnlist = list(x_data.columns[2:])
    paramColumn = paramColumn[2:]
    x_data['intercept'] = 1
    # x_data['Period'] = pd.to_datetime(x_data['Period'], format = '%Y-%m-%d')
    # endDate = x_data['Period'].max() - pd.offsets.DateOffset(months=period)
    # endYear = int(endDate.year)
    # endMonth = int(endDate.month)
    # endDay = int(calendar.monthrange(endYear,endMonth)[1])
    # limitDate = datetime(year=endYear, month=endMonth, day=endDay)
    # x_train = x_data[x_data['Period'] <= limitDate]
    # x_validate = x_data[x_data['Period'] > limitDate]

    train_size = int(len(x_data) * 0.7)
    x_train, x_validate = x_data[:train_size], x_data[train_size:]
    y_train = x_train['value1']
    y_validate = x_validate['value1']
    model = []
    predicted = {}
    predList = pd.DataFrame()
    counter = 1
    stringModel = str("m"+str(counter))
    
    # print(columnlist)
    lenVar = len(columnlist)
    
    modelCombination = len(columnlist)
    columnlist.append('intercept')
    mape_bactest=0.0
    mod = sm.OLS(y_train, x_train[columnlist])
    res = mod.fit()
    y_pred = res.predict(x_validate[columnlist])
    # y_adjrsq = res.predict(x_data[columnlist])

    period = int(len(x_validate))
    if(period>1):
        predicted["model"] = stringModel
        predicted["rsquared_validate"] = r2_score(y_validate,y_pred)
        predicted["adj_rsquared_validate"] = 1-(1-predicted["rsquared_validate"])*(x_validate.shape[0]-1)/((x_validate.shape[0]-modelCombination-1) if (x_validate.shape[0]-modelCombination-1)>0 else 1)
        #predicted["rmse_validate"] = np.sqrt(mean_squared_error(y_validate,y_pred))
        difference_y = (y_validate-y_pred)
        difference_mape = difference_y
        difference_y = [a**2 for a in difference_y]
        sum_mse = sum(difference_y)
        mse = sum_mse / (x_validate.shape[0]-modelCombination-1)
        rmse_backtest = np.sqrt(mse)
        predicted["rmse_validate"] = rmse_backtest
        predList = predList.append(predicted,ignore_index=True)
        predList["model"].fillna("m1",inplace=True)
        mape_bactest = np.mean(np.abs(difference_mape / y_validate))
    #model.append(res)
    
    mape = np.mean(np.abs(res.resid / y_train))
    tempModel = res.params.index
    params = []
    columnCounter = 1
    
    insert_mape = "{:.12f}".format(float(0 if np.isnan(mape) or np.isinf(mape) else round(mape,12)))
    insert_mape_backtest = "{:.12f}".format(float(0 if np.isnan(mape_bactest) or np.isinf(mape_bactest) else round(mape_bactest,12)))
    AdjRSQ="{:.10f}".format(float(round(res.rsquared_adj,10)))
    _RSQ_Validate=("0" if period<2 else "{:.10f}".format(float(predList[(predList['model']=='m'+str(counter))]['rsquared_validate'].values[0])))
    _AdjRSQ_Validate=("0" if period<2 else "{:.10f}".format(float(predList[(predList['model']=='m'+str(counter))]['adj_rsquared_validate'].values[0])))
    _RMSE_Validate=("0" if period<2 else "{:.10f}".format(float(predList[(predList['model']=='m'+str(counter))]['rmse_validate'].values[0])))
    _RSQ_="{:.10f}".format(float(round(res.rsquared,10)))
    RMSE="{:.10f}".format(float(round(np.sqrt(res.mse_resid),10)))
    # for j in tempModel:
    #     Estimate="{:.10f}".format(float(round(res.params[j],10)))
    #     tValue="{:.10f}".format(float(0 if np.isnan(res.tvalues[j]) or np.isinf(res.tvalues[j]) else round(res.tvalues[j],10)))
    #     Probt="{:.10f}".format(float(0 if np.isnan(res.pvalues[j]) else round(res.pvalues[j],10)))
    #     DWStatistic="{:.10f}".format(float(round(sms.durbin_watson(res.resid),10)))
    #     breushpagan="{:.10f}".format(float(round(sms.het_breuschpagan(res.resid, res.model.exog)[1],10)))
        
    #     dataInsert = ('m1', j if j=='intercept' else str(paramColumn['column_name'][columnCounter]), Estimate,
    #         Probt, AdjRSQ, ResidualNormality, insert_mape, insert_mape_backtest
    #     )
        
    #     params.append(dataInsert)
    #     columnCounter = columnCounter+1
    # returnData =pd.DataFrame(params,columns=['Model','Variable','Estimate','Probt','AdjRSQ','Residual Normality','MAPE','MAPE Backtest'])
    # dataAccuracy = ('Linear Regression',RMSE,insert_mape,AdjRSQ)
    returnAccuracy = pd.DataFrame([['Linear Regression',_RMSE_Validate,insert_mape_backtest,_AdjRSQ_Validate]], columns=['Algorithm','RMSE','MAPE','AdjRSQ'])#pd.DataFrame(dataAccuracy,columns=['RMSE','MAPE','AdjRSQ'])
    returnData = pd.DataFrame()
    returnData['Value'] = paramdf.loc[paramdf['value2'] == 'Historical']['value1']
    returnData['Data Type'] = 'Historical'
    # print(returnData)
    for_prediction = paramdf.loc[paramdf['value2'] == 'Predicted']
    for_prediction['intercept'] = 1
    y_prediction = res.predict(for_prediction[columnlist])
    y_predict_train = res.predict(x_train[columnlist])
    prediction_df = pd.DataFrame()
    prediction_df['Value'] = y_prediction
    prediction_df['Data Type'] = 'Predicted'
    returnData = returnData.append(prediction_df)
    returnData = returnData[['Data Type','Value']]
    
    len_train = range(1,len(y_predict_train)+len(y_pred)+len(y_prediction)+1)
    y_pred_join = y_predict_train
    y_pred_join = y_pred_join.append(y_pred)
    y_pred_join = y_pred_join.append(y_prediction)

    y_pred_train = y_predict_train
    y_pred_test = y_pred_join[len(y_predict_train)-1:len(y_predict_train)+len(y_pred)-1]
    y_pred_predict = y_pred_join[len(y_predict_train)+len(y_pred)-2:len(y_predict_train)+len(y_pred)+len(y_prediction)]
    import matplotlib.pyplot as plt
    
    plt.plot(len_train,paramdf['value1'], "-r", label="Historical Data")
    plt.plot(range(1,len(y_predict_train)+1),y_pred_train, "-k", label="Train Performance")
    plt.plot(range(len(y_predict_train),len(y_predict_train)+len(y_pred)),y_pred_test, "-c", label="Test Performance")
    plt.plot(range(len(y_predict_train)+len(y_pred)-1,len(y_predict_train)+len(y_pred)+len(y_prediction)+1),y_pred_predict, "-b", label="Future Performance")
    
    plt.title('Linear Regression Graph')
    # plt.xlabel('Number of Data')
    # plt.ylabel('Data comparison')
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),fancybox=True, shadow=True, ncol=5,fontsize=8)
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

    end = time.time()
    a={"Time":end-start}
    # print(a)
    if(viewParam==0):
        return returnAccuracy, plt
    else:
        return returnData, returnAccuracy, plt
