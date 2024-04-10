import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import os
matplotlib.rc('font', family='Microsoft JhengHei')

def show_plot(type):
    res1 = pd.read_excel("./temp/file.xlsx",skiprows=2,nrows=15) #如果出現 TypeError CellStyle.__init__() got an unexpected keyword argument 'xxid' 手動存一次storage裡面的檔案
    X_value = list(res1['統計期'])
    Y1_Value = list(res1["發生數(件)"])
    Y2_Value = list(res1["破獲數(件)"])
    Y3_Value = list(res1["嫌疑犯(人)"])
    Y4_Value = list(res1["被害人(人)"])

    plt.figure(figsize=(18,10),num=1)
    plt.plot(X_value,Y1_Value,label="發生數(件)")
    plt.legend()
    plt.figure(figsize=(18,10),num=1)
    plt.plot(X_value,Y2_Value,label="破獲數(件)")
    plt.legend()
    plt.figure(figsize=(18,10),num=1)
    plt.plot(X_value,Y3_Value,label="嫌疑犯(人)")
    plt.legend()
    plt.figure(figsize=(18,10),num=1)
    plt.plot(X_value,Y4_Value,label="被害人(人)")
    plt.legend()
    plt.title(type)
    #plt.show()
    
    if os.path.exists("./output/"+type+".png"):
        os.remove("./output/"+type+".png")
    plt.savefig("./output/"+type)
    