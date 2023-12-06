from matplotlib.pyplot import xlabel, ylabel
import pandas as pd
from io import BytesIO
import base64
from itertools import combinations

def scatter_trend (paramdf, paramColumn, viewParam=0):
    import matplotlib.pyplot as plt
    user_data = paramdf
    # Create object for label
    name = {}
    for i in range(len(paramColumn)):
        name["name{0}".format(i)] = paramColumn.iloc[i, paramColumn.columns.get_loc('column_name')]
    color = ['blue', 'red', 'green']
    # Create variable for number of figures
    k= 0
    # Create variable to determine number of plot if number of columns are more than 3
    combination= len((list(combinations(paramColumn.values, 2))))
    # Create plot
    if len(paramColumn) == 1:
        fig, axes = plt.subplots(nrows=1,ncols=1,figsize=(12,6))
        user_data.plot(x=user_data.columns[1], y=user_data.columns[0], ax= axes, kind="scatter", color=color[0], subplots=True, xlabel='index', ylabel=name["name"+str(0)])
    elif len(paramColumn) == 2:
        fig, axes = plt.subplots(nrows=1,ncols=1,figsize=(12,6))
        user_data.plot(x=user_data.columns[0], y=user_data.columns[1], ax= axes, kind="scatter", color=color[0], subplots=True, xlabel=name["name"+str(0)], ylabel=name["name"+str(1)])
    else:
        fig, axes = plt.subplots(nrows=1,ncols=combination,figsize=(24,6))
        for i in range(len(paramColumn)):
            for j in range(len(paramColumn)):
                if j > i:
                    user_data.plot(x=user_data.columns[i], y=user_data.columns[j], ax= axes[k], kind="scatter", color=color[k], subplots=True, xlabel=name["name"+str(i)], ylabel=name["name"+str(j)])
                    k = k+1
    
    plt.tight_layout()
    plt.show
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
    returnType = pd.DataFrame([['Scatterplot']], columns=['Type'])
    if(viewParam==0):
        return returnType,plt
    else:
        return plt