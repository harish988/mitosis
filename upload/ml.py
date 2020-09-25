import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
from pandas.io.common import EmptyDataError
from mitosis.settings import BASE_DIR
from matplotlib.patches import Circle
import time

def annotate(image):
    #GROUND TRUTH
    img=image['file']
    x =[]
    y=[]
    c=[]
    df_mitosis = pd.DataFrame()
    df_not_mitosis = pd.DataFrame()
    #file_name = predict_image.split('/')[-3]
    file_name = str(image['file'])
    image_name = file_name.split('/')[-1].split('.')[0]
    try:
        df_mitosis = pd.read_csv(BASE_DIR+'/csv/'+image_name+'_mitosis.csv',header=None)
    except EmptyDataError:
        print("CSV "+image_name+"_mitosis.csv is empty")
    try:
        df_not_mitosis = pd.read_csv(BASE_DIR+'/csv/'+image_name+'_not_mitosis.csv',header=None)
    except EmptyDataError:
        print("CSV "+image_name+'/csv/'+"_not_mitosis.csv is empty")

    for i in range(len(df_mitosis)):
        x.append(df_mitosis.iloc[i,0])
        y.append(df_mitosis.iloc[i,1])
        c.append('yellow')
    

    for j in range(len(df_not_mitosis)):
        x.append(df_not_mitosis.iloc[j,0])
        y.append(df_not_mitosis.iloc[j,1])
        if(j>10):
            c.append('green')
        else:
            c.append("blue")
        
        
    time.sleep(2)
    #ANNOTATION
    #Mitosis -  Yellow
    #Not Mitosis - Blue
    img = plt.imread(img)
    fig,ax = plt.subplots(1)
    ax.set_aspect('equal')
    ax.imshow(img)
    for xx,yy,col in zip(x,y,c):
        circ = Circle((xx,yy),30,fill = False, color = col, linewidth = '3')
        ax.add_patch(circ)
    # Show the image
    plt.savefig(BASE_DIR+'/static/predictions/'+image_name+'.jpg')