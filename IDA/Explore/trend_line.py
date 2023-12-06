import pandas as pd
from io import BytesIO
import base64

def line_trend (paramdf, paramColumn, viewParam=0):
    import matplotlib.pyplot as plt
    user_data = paramdf
    user_data['new'] = range(1, len(user_data) +1)
    user_data = user_data.reset_index()
    x = user_data['new']
    # Create object for label
    d = {}
    for i in range(len(paramColumn)):
        d["name{0}".format(i)] = paramColumn.iloc[i, paramColumn.columns.get_loc('column_name')]
    color = ['blue', 'red', 'green']
    # Create plot
    fig, ax = plt.subplots(figsize=(12,4))
    if len(paramColumn) ==1:
        plt.plot(x, user_data.value1, label = d['name'+str(0)], color=color[0])
        plt.legend(bbox_to_anchor=(1.2, 1))
    elif len(paramColumn) == 2:
        fig.subplots_adjust(right=0.7)
        user_data.value1.plot(ax=ax, style='b-')
        user_data.value2.plot(ax=ax, style='r-', secondary_y=True)
        ax.legend([ax.get_lines()[0], ax.right_ax.get_lines()[0]],[d['name'+str(0)], d['name'+str(1)]], bbox_to_anchor=(1.3, 1))
    elif len(paramColumn) == 3:
        ax3 = ax.twinx()
        rspine = ax3.spines['right']
        rspine.set_position(('axes', 1))
        ax3.set_frame_on(True)
        ax3.patch.set_visible(False)
        fig.subplots_adjust(right=0.7)

        user_data.value1.plot(ax=ax, style='b-')
        user_data.value2.plot(ax=ax, style='r-', secondary_y=True)
        user_data.value3.plot(ax=ax3, style='g-')
        ax3.legend([ax.get_lines()[0], ax.right_ax.get_lines()[0], ax3.get_lines()[0]],[d['name'+str(0)], d['name'+str(1)], d['name'+str(2)]], bbox_to_anchor=(1.5, 1))

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
    returnType = pd.DataFrame([['Line']], columns=['Type'])
    if(viewParam==0):
        return returnType,plt
    else:
        return plt