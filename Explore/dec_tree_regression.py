from math import sqrt
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from io import BytesIO
from sklearn.tree import DecisionTreeRegressor
import numpy as np
import pandas as pd
import base64


def calculate_dectree_regress(paramdf, paramColumn, viewParam=0):
	# dataset = pd.read_excel('D:\Work\Python\dec_tree_regress_test.xlsx')
	dataset = paramdf
	datasetHistorical = dataset.loc[dataset['value2'] == 'Historical']

	#define x variable
	X=datasetHistorical.iloc[:, 2:len(datasetHistorical.columns)]

	#define y variable
	y=datasetHistorical.iloc[:, 0]

	train_size = int(len(datasetHistorical) * 0.7)

	# Split dataset
	X_train, X_test = X[:train_size], X[train_size:]
	y_train, y_test = y[:train_size], y[train_size:]



	# create a regressor object
	regressor = DecisionTreeRegressor() 
	  
	# fit the regressor with X and Y data
	regressor.fit(X_train, y_train)

	# predict test data
	predictions = regressor.predict(X_test)

	# predicting a new value
	X_Pred = dataset.loc[dataset['value2'] == 'Predicted']
	X_Pred = X_Pred.iloc[:, 2:len(X_Pred.columns)]
	# test the output by changing values, like 3750
	y_pred = regressor.predict(X_Pred)


	# Calculate mean absolute percentage error (MAPE)
	mape = np.mean(np.abs(((y_test - predictions) / y_test)))
	# Calculate RMSE
	rmse = sqrt(mean_squared_error(y_test, predictions))
	# Calculate Adj Sqrt
	r2 = r2_score(y_test, predictions)
	Adj_r2 = 1 - (1-r2_score(y_test, predictions)) * (len(y_test)-1)/(len(y_test)-X.shape[1]-1)

	# Define the feature for predictions
	pred_feat = dataset.iloc[:, 2:len(dataset.columns)]
	# Predict the prediction feature
	pred = regressor.predict(pred_feat)
	len_train = range(len(X))
	len_pred = range(len(dataset))
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
	plt.title('Decision Tree Regression Graph')
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
	returnAccuracy = pd.DataFrame([['Decision Tree',rmse,mape,Adj_r2]], columns=['Algorithm','RMSE','MAPE','AdjRSQ'])
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