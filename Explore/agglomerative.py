import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler, normalize
from sklearn.metrics import silhouette_score
import scipy.cluster.hierarchy as shc
from mpl_toolkits import mplot3d
from PIL import Image, ImageDraw
import base64
from io import BytesIO

def calculate_agglomerative (paramdf, paramColumn, viewParam=0):
    user_data = paramdf
    user_data.columns = list(paramColumn.iloc[:,0])
   
    
    # Scaling the data so that all the features become comparable
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(user_data)
      
    # Normalizing the data so that the data approximately 
    # follows a Gaussian distribution
    X_normalized = normalize(X_scaled)
      
    # Converting the numpy array into a pandas DataFrame
    X_normalized = pd.DataFrame(X_normalized)
    ac3 = AgglomerativeClustering(n_clusters = 3)
    # c = ac3.fit_predict(X_principal)
    c = ac3.fit_predict(X_normalized)
    c = pd.DataFrame(c,columns=['cluster'])

    dataset= pd.concat([user_data, c], axis=1)
    data1 = dataset[dataset.cluster==0]
    data2 = dataset[dataset.cluster==1]
    data3 = dataset[dataset.cluster==2]

    if user_data.shape[1]==1:
        dataset.insert(1,'constant',1)
        data1 = dataset[dataset.cluster==0]
        data2 = dataset[dataset.cluster==1]
        data3 = dataset[dataset.cluster==2]
        import matplotlib.pyplot as plt
        plt.scatter(data1.iloc[:,1],data1.iloc[:,0], c='blue', label = 'Cluster 0')
        plt.scatter(data2.iloc[:,1],data2.iloc[:,0], c='red', label = 'Cluster 1')
        plt.scatter(data3.iloc[:,1],data3.iloc[:,0], c='yellow', label = 'Cluster 2')
        plt.title("Agglomerative")
        plt.legend()
        plt.xlabel(dataset.columns[1])
        plt.ylabel(dataset.columns[0])

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
    elif user_data.shape[1]==2:
        import matplotlib.pyplot as plt
        plt.scatter(data1.iloc[:,0],data1.iloc[:,1], c='blue', label = 'Cluster 0')
        plt.scatter(data2.iloc[:,0],data2.iloc[:,1], c='red', label = 'Cluster 1')
        plt.scatter(data3.iloc[:,0],data3.iloc[:,1], c='yellow', label = 'Cluster 2')
        plt.title("Agglomerative")
        plt.legend()
        plt.xlabel(dataset.columns[0])
        plt.ylabel(dataset.columns[1])

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
    elif user_data.shape[1]==3:
        import matplotlib.pyplot as plt
        kplot = plt.axes(projection='3d')
        kplot.scatter3D(data1.iloc[:,0],data1.iloc[:,1],data1.iloc[:,2], c='blue', label = 'Cluster 0')
        kplot.scatter3D(data2.iloc[:,0],data2.iloc[:,1],data2.iloc[:,2], c='red', label = 'Cluster 1')
        kplot.scatter3D(data3.iloc[:,0],data3.iloc[:,1],data3.iloc[:,2], c='yellow', label = 'Cluster 2')
        plt.title("Agglomerative")
        plt.legend()
        kplot.set_xlabel(dataset.columns[0])
        kplot.set_ylabel(dataset.columns[1])
        kplot.set_zlabel(dataset.columns[2])

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
    elif user_data.shape[1]>3:
        plt=''
    
    returnAlgo = pd.DataFrame([['Agglomerative']], columns=['Algorithm'])

    if(viewParam==0):
        return returnAlgo,plt
    else:
        return dataset, plt