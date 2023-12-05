import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
from PIL import Image, ImageDraw
from math import sqrt
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import base64
from io import BytesIO

def calculate_knnregr (paramdf, paramColumn, viewParam=0):
    user_data = paramdf
    # user_data.columns = list(paramColumn.iloc[:,0])
    for i in range(len(paramColumn)):
        user_data = user_data.rename(columns={ user_data.columns[i]: paramColumn['column_name'][i] })

    
    #drop the rows that will be predicted
    dataset = paramdf.loc[paramdf['value2'] == 'Historical']

    #define x variable
    X=dataset.iloc[:, 2:len(dataset.columns)]

    #define y variable
    y=dataset.iloc[:, 0]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

    scaler = StandardScaler()
    scaler.fit(X_train)

    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    regression = KNeighborsRegressor(n_neighbors=5)
    regression.fit(X_train, y_train)
    y_pred = regression.predict(X_test)

    mape = np.mean(np.abs(((y_test - y_pred) / y_test)))
    # Calculate RMSE
    rmse = sqrt(mean_squared_error(y_test, y_pred))
    # Calculate Adj Sqrt
    r2 = r2_score(y_test, y_pred)
    # Adj_r2 = 1 - (1-r2_score(y_test, predictions)) * (len(y)-1)/(len(y)-X.shape[1]-1)
    Adj_r2 = 1 - (1-r2_score(y_test, y_pred)) * (len(y_test)-1)/(len(y_test)-X_test.shape[1]-1)
    
    df_accuracy=pd.DataFrame([['K Nearest Neighbor',rmse,mape,Adj_r2]], columns=['Algorithm','RMSE','MAPE','AdjRSQ'])
    #select rows to predict
    for_prediction = paramdf.loc[paramdf['value2'] == 'Predicted']

    #seperate column 
    for_prediction_valtype=for_prediction.iloc[:,1]
    for_prediction=for_prediction.iloc[:,2:len(for_prediction.columns)]

    prediction=regression.predict(for_prediction)
    prediction= pd.DataFrame({paramdf.columns[0]: prediction})

    for_prediction_valtype.reset_index(drop=True, inplace=True)
    prediction.reset_index(drop=True, inplace=True)
    df_prediction = pd.concat( [for_prediction_valtype, prediction], axis=1)

    returnData = pd.concat( [dataset.iloc[:,1],dataset.iloc[:,0]], axis=1)
    returnData=pd.concat([returnData, df_prediction], ignore_index=True)
    returnData.rename(columns={returnData.columns[0]: 'Data Type', returnData.columns[1]: 'Value'},inplace=True)
    
    #visualization
    X_graph=user_data.iloc[:, 2:len(user_data.columns)]
    y_pred_graph = regression.predict(X_graph)
    y_pred_graph = pd.DataFrame({'Predicted': y_pred_graph})

    import matplotlib.pyplot as plt
    plt.plot(range(len(y)), y, 'r-', label = 'Historical Data')
    plt.plot(range(len(y_pred_graph)), y_pred_graph['Predicted'], 'b-', label = 'Prediction Data')
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), fancybox=True, shadow=True, ncol=5)
    plt.title('K Nearest Neighbor Graph')
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
        return df_accuracy, plt
    else:
        return returnData, df_accuracy, plt