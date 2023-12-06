import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix

def calculate_knn (paramdf, paramColumn, viewParam=0):
    user_data = paramdf
    print(user_data)
    print(paramColumn)
    user_data.columns = list(paramColumn.iloc[:,0])
    #drop the rows that will be predicted
    dataset = user_data.dropna(subset=[user_data.columns[0]])
    
    #define x variable
    X=dataset.iloc[:, 1:len(dataset.columns)]

    #define y variable
    y=dataset.iloc[:, 0]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

    scaler = StandardScaler()
    scaler.fit(X_train)

    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    classifier = KNeighborsClassifier(n_neighbors=5)
    classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)
    # df_y = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})

    accuracy = classification_report(y_test, y_pred, output_dict=True)
    df_accuracy = pd.DataFrame(accuracy).transpose()
    df_accuracy = df_accuracy.iloc[:-3,:].round(2)
    df_accuracy = df_accuracy.rename(columns={'f1-score': 'f1Score'})
    df_accuracy['Algorithm'] = 'KNN'

    #select rows to predict
    for_prediction = user_data[user_data.iloc[:,0].isna()]
    #drop y variable
    for_prediction=for_prediction.iloc[:,1:len(for_prediction.columns)]
    prediction=classifier.predict(for_prediction)
    prediction= pd.DataFrame({user_data.columns[0]: prediction})

    for_prediction.reset_index(drop=True, inplace=True)
    prediction.reset_index(drop=True, inplace=True)
    df_prediction = pd.concat( [prediction,for_prediction], axis=1)

    historicalData = dataset
    historicalData = historicalData.rename(columns={ historicalData.columns[0]: user_data.columns[0] })

    # for i in range(len(list(paramColumn.iloc[:,0]))):
    #     historicalData = historicalData.rename(columns={ historicalData.columns[i+1]: str(list(paramColumn.iloc[:,0])[i]) })
    
    historicalData['Data Type'] = 'Historical'
    df_prediction['Data Type'] = 'Predicted'

    returnData = historicalData
    returnData = returnData.append(df_prediction)

    cols = returnData.columns.tolist()
    cols = [cols[-1]] + cols[:-1]
    returnData = returnData[cols]
    if(viewParam==0):
        return df_accuracy
    else:
        return df_accuracy, returnData