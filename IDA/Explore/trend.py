import numpy as np

import pandas as pd
from io import BytesIO
import base64

def see_trend (paramdf, paramColumn, viewParam=0):
    user_data = paramdf
    listColumn = list(paramColumn)
    for i in range(len(listColumn)):
        user_data = user_data.rename(columns={ user_data.columns[i]: listColumn[i] })
    # user_data.columns = list(paramColumn.iloc[:,0])
    #drop the rows that will be predicted
    # dataset = paramdf.loc[paramdf['value2'] == 'Historical']
    dataset = paramdf
    #define x variable
    X=dataset.iloc[:, 1:len(dataset.columns)]

    #define y variable
    y=dataset.iloc[:, 0]
    returnType = pd.DataFrame([['Line']], columns=['Type'])
    import matplotlib.pyplot as plt

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
        return returnType,plt
    else:
        return plt