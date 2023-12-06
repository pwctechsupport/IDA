import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

def rf_class(paramdf, paramColumn, viewParam=0):
    user_data = paramdf
    # Drop the rows that will be predicted
    # dataset = user_data.dropna(subset=[user_data.columns[0]])
    dataset = user_data.loc[paramdf['value2'] == 'Historical']
    # Define x & y variable
    X=dataset.iloc[:, 2:len(dataset.columns)]
    y=dataset.iloc[:, 0]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

    # Create Random Forest model for Classification
    rf = RandomForestClassifier(n_estimators = 1000, random_state=42)
    # Train the model on training data
    rf.fit(X_train, y_train)
    # Predict the model using test data
    y_pred = rf.predict(X_test)

    # Compute precision, recall, f1-score, support
    accuracy = classification_report(y_test,y_pred, output_dict=True)

    # Create df_accuracy for return value
    df_accuracy = pd.DataFrame(accuracy).transpose()
    df_accuracy = df_accuracy.iloc[:-3,:].round(2)
    df_accuracy = df_accuracy.rename(columns={'f1-score': 'f1Score'})
    df_accuracy['Algorithm'] = 'Random Forest'

    # Select and predict for predict data
    # for_prediction = user_data[user_data.iloc[:,0].isna()]
    for_prediction = user_data.loc[user_data['value2'] == 'Predicted']
    # Drop y value
    for_prediction=for_prediction.iloc[:,2:len(for_prediction.columns)]
    
    prediction=rf.predict(for_prediction)
    
    # Create dataframe for predict
    prediction= pd.DataFrame({user_data.columns[0]: prediction})
    for_prediction.reset_index(drop=True, inplace=True)
    prediction.reset_index(drop=True, inplace=True)
    df_prediction = pd.concat( [prediction, for_prediction], axis=1)

    # Insert Predicted to df_predicition
    df_prediction.insert(1,'value2','Predicted')
    
    # Concat dataset with df_prediction
    data=pd.concat([dataset, df_prediction], ignore_index=True)
    data.columns=list(paramColumn.iloc[:,0])
    if(viewParam==0):
        return df_accuracy
    else:
        return df_accuracy, data