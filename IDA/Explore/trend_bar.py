import pandas as pd
from io import BytesIO
import base64

def bar_trend (paramdf, paramColumn, viewParam=0):
    import matplotlib.pyplot as plt
    user_data = paramdf
    # Create new column for index
    user_data['new'] = range(1, len(user_data) +1)
    user_data = user_data.reset_index()
    x = user_data['new']
    # Create object for label
    name = {}
    for i in range(len(paramColumn)):
        name["name{0}".format(i)] = paramColumn.iloc[i, paramColumn.columns.get_loc('column_name')]
    color = ['blue', 'red', 'green']

    # Create plot
    ax = plt.subplot(111)  
    space = 0.2
    for i in range(len(paramColumn)):
        ax.bar(x-space, user_data['value'+str(i+1)], width=0.2, color=color[i], align='center', label=name['name'+str(i)])
        space += 0.2

    # Show legend and plot
    ax.legend(loc='center left', bbox_to_anchor=(1, 1))
    plt.tight_layout()
    plt.gcf().set_size_inches(10, 4)
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
    returnType = pd.DataFrame([['Bar']], columns=['Type'])
    if(viewParam==0):
        return returnType,plt
    else:
        return plt