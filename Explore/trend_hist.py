from unicodedata import name
from matplotlib.pyplot import title, ylabel
import pandas as pd
from io import BytesIO
import base64

def hist_trend (paramdf, paramColumn, viewParam=0):
    import matplotlib.pyplot as plt
    user_data = paramdf
    
    # Create object for label
    name = {}
    for i in range(len(paramColumn)):
        name["name{0}".format(i)] = paramColumn.iloc[i, paramColumn.columns.get_loc('column_name')]
    color = ['blue', 'red', 'green']
    
    # Creating histogram
    if len(paramColumn) == 1:
        fig, ax = plt.subplots(nrows=1,ncols=(len(paramColumn)),figsize=(12,6))
        ax.hist(user_data['value1'], 4, histtype='bar', color=color[0])
        ax.set_title(name["name"+str(0)])
        ax.set_ylabel('Frequency')
    else:
        fig, ax = plt.subplots(nrows=1,ncols=(len(paramColumn)),figsize=(24,6))
        for i in range(len(paramColumn)):
            ax[i].hist(user_data['value'+str(i+1)], 4, histtype='bar', color=color[i])
            ax[i].set_title(name["name"+str(i)])
            ax[i].set_ylabel('Frequency')
    
    # Show plot
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
    returnType = pd.DataFrame([['Histogram']], columns=['Type'])
    if(viewParam==0):
        return returnType,plt
    else:
        return plt