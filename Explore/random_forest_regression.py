import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn.metrics import r2_score
from io import BytesIO
import base64

def rf_regression(paramdf, paramColumn, viewParam=0):
    user_data = paramdf
    # Drop the rows that will be predicted
    dataset = user_data.loc[user_data['value2'] == 'Historical']
                           
    # Define x variable
    X=dataset.iloc[:, 2:len(dataset.columns)]
    # Define y variable
    y=dataset.iloc[:, 0]

    train_size = int(len(dataset) * 0.7)

    # Split dataset
    X_train, X_test = X[:train_size], X[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]

    # Instantiate model with 1000 decision trees
    rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
    # Train the model on training data
    rf.fit(X_train, y_train);
    # Use the forest's predict method on the test data
    predictions = rf.predict(X_test)

    # Calculate mean absolute percentage error (MAPE)
    mape = np.mean(np.abs(((y_test - predictions) / y_test)))
    # Calculate RMSE
    rmse = sqrt(mean_squared_error(y_test, predictions))
    # Calculate Adj Sqrt
    r2 = r2_score(y_test, predictions)
    # Adj_r2 = 1 - (1-r2_score(y_test, predictions)) * (len(y)-1)/(len(y)-X.shape[1]-1)
    Adj_r2 = 1 - (1-r2_score(y_test, predictions)) * (len(y_test)-1)/(len(y_test)-X.shape[1]-1)
    # Define the feature for predictions
    pred_feat = paramdf.iloc[:, 2:len(paramdf.columns)]
    # Predict the prediction feature
    pred = rf.predict(pred_feat)

    # Define the length of dataset
    len_train = range(len(X))
    len_pred = range(len(paramdf))

    
    # Dataframe for true value
    true_data = pd.DataFrame(data = {'actual': y})
    # Dataframe for predictions
    predictions_data = pd.DataFrame(data = {'prediction': pred})

    import matplotlib.pyplot as plt
    # Set the style
    # plt.style.use('fivethirtyeight')
    # Plot the actual value
    plt.plot(len_train, true_data['actual'], 'r-', label = 'Historical Data')
    # Plot the predicted value
    plt.plot(len_pred, predictions_data['prediction'], 'b-', label = 'Prediction Data')
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), fancybox=True, shadow=True, ncol=5)
    # Graph labels
    plt.title('Random Forest Regression Graph')
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

    # Define returnAccuracy
    returnAccuracy = pd.DataFrame([['Random Forest',rmse,mape,Adj_r2]], columns=['Algorithm','RMSE','MAPE','AdjRSQ'])
    # Define returnData
    # Historical Data
    returnData = pd.DataFrame()
    returnData['Value'] = paramdf.loc[paramdf['value2'] == 'Historical']['value1']
    returnData['Data Type'] = 'Historical'
    # Prediction Data
    for_prediction = predictions_data.iloc[len(y):,0]
    prediction_df = pd.DataFrame()
    prediction_df['Value'] = for_prediction
    prediction_df['Data Type'] = 'Predicted'
    returnData = returnData.append(prediction_df)
    returnData = returnData[['Data Type','Value']]
    if(viewParam==0):
        return returnAccuracy, plt
    else:
        return returnData, returnAccuracy, plt
