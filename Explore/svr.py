import numpy as np

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from io import BytesIO
import base64

def calculate_svr (paramdf, paramColumn, viewParam=0):
    user_data = paramdf
    listColumn = list(paramColumn)
    for i in range(len(listColumn)):
        user_data = user_data.rename(columns={ user_data.columns[i]: listColumn[i] })
    # user_data.columns = list(paramColumn.iloc[:,0])
    #drop the rows that will be predicted
    dataset = paramdf.loc[paramdf['value2'] == 'Historical']
    
    #define x variable
    X=dataset.iloc[:, 2:len(dataset.columns)]

    #define y variable
    y=dataset.iloc[:, 0]
    
    train_size = int(len(dataset) * 0.7)

    # Split dataset
    X_train, X_test = X[:train_size], X[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

    model = SVR(kernel = 'linear')
    model.fit(X_train,y_train)

    y_train_predictions = model.predict(X_train)
    MSE = mean_squared_error(y_train, y_train_predictions)
    RMSE = np.sqrt(MSE)

    y_test_predictions = model.predict(X_test) 

    MAPE = np.mean(np.abs((y_test - y_test_predictions)/y_test))
    # print(y_test)
    # print(y_test_predictions)

    AdjRSQ =  1 - (1 - r2_score(y_test, y_test_predictions)) * (len(X_test)-1)/(len(X_test)-(X_test.shape[1])-1)
    # AdjRSQ = 0
    returnAccuracy = pd.DataFrame([['Support Vector Regression',RMSE,MAPE,AdjRSQ]], columns=['Algorithm','RMSE','MAPE','AdjRSQ'])

    for_prediction = paramdf.loc[paramdf['value2'] == 'Predicted']
    for_prediction=for_prediction.iloc[:,2:len(for_prediction.columns)]
    prediction=model.predict(for_prediction)
    prediction_list = prediction.tolist()
    prediction= pd.DataFrame({'Value': prediction})

    for_prediction.reset_index(drop=True, inplace=True)
    prediction.reset_index(drop=True, inplace=True)
    # df_prediction = pd.concat( [prediction,for_prediction], axis=1)

    historicalData = pd.DataFrame({'Value': dataset['value1']})
    # historicalData = historicalData.rename(columns={ historicalData.columns[0]: "Value" })
 
    historicalData['Data Type'] = 'Historical'
    prediction['Data Type'] = 'Predicted'
    # df_prediction['Data Type'] = 'Predicted'
    # print(historicalData)
    # print(df_prediction)

    returnData = historicalData
    returnData = returnData.append(prediction)
    cols = returnData.columns.tolist()
    cols = [cols[-1]] + cols[:-1]
    returnData = returnData[cols]

    len_predict = range(1,len(y_train_predictions)+len(y_test_predictions)+len(prediction)+1)
    len_historical = range(1,len(historicalData)+1)
    y_pred_join = y_train_predictions.tolist()
    y_pred_join.extend(y_test_predictions.tolist())
    y_pred_join.extend(prediction_list)
    # print(len_predict)
    # print(len_historical)
    # print(y_pred_join)
    # print(paramdf['value1'])
    import matplotlib.pyplot as plt
    
    plt.plot(len_historical,historicalData['Value'], "-r", label="Historical Data")
    plt.plot(len_predict,y_pred_join, "-b", label="Prediction Data")
    plt.title('Support Vector Regression Graph')
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
    if(viewParam==0):
        return returnAccuracy, plt
    else:
        return returnData, returnAccuracy, plt