# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import rcParams
import os
#產生長條圖
def show_barchart(excel_path):
    
    rcParams['font.sans-serif'] = 'SimSun'
    crime=pd.read_excel(excel_path)
    #crime=flip1.retrieve(r"C:\Users\asus\OneDrive\桌面\python\temp\file111.xlsx",r"C:\Users\asus\OneDrive\桌面\python\temp\newfile.xlsx")
    #將無法轉換為數值的值轉為NaN
    crime[4] = pd.to_numeric(crime[4],errors='coerce')
    #將包含NaN的行刪除
    crime = crime.dropna(subset=[4])
    #刪除機關別總計
    
    #更改x軸細項名字
    plt.bar(list(range(1,crime.shape[0]+1)),crime[4])
    plt.xticks(list(range(1,crime.shape[0]+1)),list(crime[3]),rotation=45)
    #更該xy軸標籤
    plt.xlabel("縣市")
    plt.ylabel("發破率")
    if os.path.exists("./temp/barchart.png"):
        os.remove("./temp/barchart.png")
    plt.savefig("./temp/barchart.png")
    plt.show()
if __name__ == "__main__":
    show_barchart()
    