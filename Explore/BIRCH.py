
from sklearn.cluster import Birch
import pandas as pd
from sklearn.preprocessing import StandardScaler
from io import BytesIO
import base64

def birch_cluster(paramdf, paramColumn, viewParam=0):
    user_data = paramdf
    user_data.columns = list(paramColumn.iloc[:,0])

    # Create transformed Dataset
    scaler = StandardScaler()
    scaler.fit(user_data)
    X = scaler.transform(user_data)

    # Create and Initialize(Fit) BIRCH model
    model = Birch(branching_factor = 100, n_clusters = 3, threshold = 0.5)
    model.fit(X)

    # Predict model
    y = model.predict(X)

    # Create y1 variable to save cluster value
    y1 = pd.DataFrame(y,columns=['cluster'])

    # Concat y1 to user_data to create new dataset, Create data1, data2, data3 to split dataset based on cluster value
    dataset = pd.concat([user_data, y1], axis=1)
    data1 = dataset[dataset.cluster==0]
    data2 = dataset[dataset.cluster==1]
    data3 = dataset[dataset.cluster==2]
    
    import matplotlib.pyplot as plt
    # Create plt to show cluster on scatter plot
    plt.scatter(data1.iloc[:,0],data1.iloc[:,1], c='blue', label = 'Cluster 0')
    plt.scatter(data2.iloc[:,0],data2.iloc[:,1], c='red', label = 'Cluster 1')
    plt.scatter(data3.iloc[:,0],data3.iloc[:,1], c='yellow', label = 'Cluster 2')
    plt.title("BIRCH")
    plt.legend()
    plt.xlabel(dataset.columns[1])
    plt.ylabel(dataset.columns[0])

    # Save plt model into png
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

    returnAlgo = pd.DataFrame([['BIRCH']], columns=['Algorithm'])

    if(viewParam==0):
        return returnAlgo,plt
    else:
        return dataset, plt