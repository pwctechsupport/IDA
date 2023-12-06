import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
from io import BytesIO
import base64

def stat_trend (paramdf, paramColumn, viewParam=0):
    import matplotlib.pyplot as plt
    from statsmodels.tsa.seasonal import seasonal_decompose
    user_data = paramdf
    # Create object for label
    name = {}
    for i in range(len(paramColumn)):
        name["name{0}".format(i)] = paramColumn.iloc[i, paramColumn.columns.get_loc('column_name')]
    color = ['blue', 'red', 'green']
    # Create new column for index
    user_data['new'] = range(1, len(user_data) +1)
    user_data = user_data.reset_index()
    x = user_data['new'].all()

    # Function for create seasonal plot
    def plotseasonal(res, axes, title, colors): 
        res.observed.plot(ax=axes[0], legend=False, color=colors)
        axes[0].set_ylabel('Observed')
        res.trend.plot(ax=axes[1], legend=False, color=colors)
        axes[1].set_ylabel('Trend')
        res.seasonal.plot(ax=axes[2], legend=False, color=colors)
        axes[2].set_ylabel('Seasonal')
        res.resid.plot(ax=axes[3], legend=False, color=colors)
        axes[3].set_ylabel('Residual')
        axes[3].set_xlabel(title)

    color = ['blue', 'red', 'green']
    # Create plot
    if len(paramColumn) == 1:
        fig, axes = plt.subplots(ncols=(len(paramColumn)), nrows=4, figsize=(14,12))
        plotseasonal(seasonal_decompose(user_data['value1'], freq=12), axes[:], name["name"+str(0)], color[0])
    else:
        fig, axes = plt.subplots(ncols=(len(paramColumn)), nrows=4, figsize=(24,12))
        for i in range(len(paramColumn)):
            plotseasonal(seasonal_decompose(user_data['value'+str(i+1)], freq=12), axes[:,i], name["name"+str(i)], color[i])

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
    returnType = pd.DataFrame([['Stationary']], columns=['Type'])
    if(viewParam==0):
        return returnType,plt
    else:
        return plt