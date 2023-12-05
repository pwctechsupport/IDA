from sklearn.cluster import DBSCAN
import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from io import BytesIO
import base64

def dbscan_cluster(paramdf, paramColumn, viewParam=0):
    user_data = paramdf
    user_data.columns = list(paramColumn.iloc[:,0])

    # Create transformed Dataset
    scaler = StandardScaler()
    scaler.fit(user_data)
    X = scaler.transform(user_data)

    # Create and Initialize(Fit) BIRCH model
    model = DBSCAN(eps=0.3, min_samples=20)
   

    # Predict model
    y = model.fit_predict(X, sample_weight=3)
    y1 = pd.DataFrame(y,columns=['cluster'])
    
    core_samples_mask = np.zeros_like(model.labels_, dtype=bool)
    core_samples_mask[model.core_sample_indices_] = True
    labels = model.labels_
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
    n_noise_ = list(labels).count(-1)

    print("Estimated number of clusters: %d" % n_clusters_)
    print("Estimated number of noise points: %d" % n_noise_)    

    dataset = pd.concat([user_data, y1], axis=1)
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 7), dpi=80)

    for x in range(n_clusters_ + 1):
      data = 'data' + str(x)
      if data == 'data0':
        data = dataset[dataset.cluster==x-1]
        plt.scatter(data.iloc[:,0],data.iloc[:,1], label = 'Noise')
      else:
        data = dataset[dataset.cluster==x-1]
        plt.scatter(data.iloc[:,0],data.iloc[:,1], label = 'Cluster' + str(x-1))
    plt.title("DBSAN Clustering")
    
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

    returnAlgo = pd.DataFrame([['DBSCAN']], columns=['Algorithm'])

    if(viewParam==0):
        return returnAlgo,plt
    else:
        return dataset, plt