import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import classification_report, confusion_matrix

def calculate_svm (paramdf, paramColumn, viewParam=0):
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

    scaler = MinMaxScaler(feature_range = (0,1))
    scaler.fit(X_train)

    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    classifier = SVC(kernel='linear')
    classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)

    accuracy = classification_report(y_test, y_pred, output_dict=True)
    df_accuracy = pd.DataFrame(accuracy).transpose()
    df_accuracy = df_accuracy.iloc[:-3,:].round(2)
    df_accuracy = df_accuracy.rename(columns={'f1-score': 'f1Score'})
    df_accuracy['Algorithm'] = 'SVM'

    #select rows to predict
    for_prediction = paramdf.loc[paramdf['value2'] == 'Predicted']

    #drop y variable
    for_prediction=for_prediction.iloc[:,2:len(for_prediction.columns)]
    prediction=classifier.predict(for_prediction)
    prediction= pd.DataFrame({paramdf.columns[0]: prediction,paramdf.columns[1]:'Predicted'})
    for_prediction.reset_index(drop=True, inplace=True)
    prediction.reset_index(drop=True, inplace=True)
    df_prediction = pd.concat( [prediction,for_prediction], axis=1)
    returnData=pd.concat([dataset, df_prediction], ignore_index=True)
    returnData.columns=list(paramColumn.iloc[:,0])
    if(viewParam==0):
        return df_accuracy
    else:
        return df_accuracy, returnData