# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 23:01:18 2023

@author: USER
"""

import tkinter as tk
from tkinter import ttk
import download_barchart as db
import web_crawler3 as wc
import flip1 as f
import cmap 
import barchart as bar
import reader as read
import test_excel as te
import openpyxl
import os

state = 0
URL = "https://ba.npa.gov.tw/statis/webMain.aspx?k=defjsp" #如果哪天統計網出問題就要改它
download_folder = "C:/Users/jimmy/Downloads"
afterprocessing="./temp/newfile.xlsx"
os.chdir(os.path.dirname(__file__))

def on_button_click(category, crime_type, city_or_year_var):
    print(f"您選擇的是 {city_or_year_var.get()}, 犯罪類型是：{category} - {crime_type}")
    target=f"{crime_type}"
    print(target)
    if f"{city_or_year_var.get()}"=="歷年":
        #下載歷年檔案
        year(target,URL,download_folder)
    else:
        city(target,URL,download_folder,afterprocessing)

def year(target,URL,download_folder):
    state = wc.crawl(target,URL)
    if state == 0:
        wc.to_storage(target,download_folder)
        te.processing()
        read.show_plot(target)

def city(target,URL,download_folder,afterprocessing):
    #下載縣市檔案
    db.Download(target,URL)
    #找到最新檔案重新命名
    new_path=f.rename(download_folder)
    #開檔重新儲存
    te.processing()
    #轉置擷取檔案至新檔案
    new_file=f.retrieve(new_path,afterprocessing)
    file_path="./temp/newfile.xlsx"
    #匯出長條圖
    bar.show_barchart(file_path)
    #匯出地圖
    cmap.cmap(file_path)

def end_program(root):
    print("結束")
    root.destroy()

def create_gui():
    root = tk.Tk()
    root.title("Taiwan Crime Data")

    title_label = ttk.Label(root, text="Step 1: 選擇縣市或歷年", font=("Helvetica", 16))
    title_label.grid(row=0, column=0, columnspan=4, pady=(10, 20))

    # 第一步驟: 選擇縣市或歷年
    option_values_city_or_year = ["縣市", "歷年"]
    city_or_year_var = tk.StringVar()
    city_or_year_var.set(option_values_city_or_year[0])

    city_or_year_combobox = ttk.Combobox(root, values=option_values_city_or_year, textvariable=city_or_year_var, state="readonly")
    city_or_year_combobox.grid(row=1, column=0, columnspan=4, pady=(0, 20))

    title_label = ttk.Label(root, text="Step 2: 選擇犯罪類型", font=("Helvetica", 16))
    title_label.grid(row=2, column=0, columnspan=4, pady=(10, 20))

    # 第二步驟: 選擇犯罪類型
    option_values_crime_type = {
         "暴力犯罪": ["故意殺人", "擄人勒贖", "強盜","重大恐嚇取財"],
        "治安相關": ["一般傷害", "一般恐嚇取財","性侵害"],
        "普通刑法案": ["賭博", "妨害自由", "偽造文書印文"],
        "特別刑法案": ["違反著作權法", "違反選罷法", "違反商標法"]
    }

    for i, (category, crime_types) in enumerate(option_values_crime_type.items()):
        button_frame = ttk.Frame(root, padding="10")
        button_frame.grid(row=i + 3, column=0, padx=10, pady=10)

        button_label = ttk.Label(button_frame, text=category)
        button_label.grid(row=0, column=0, columnspan=4, pady=(0, 5))

        for j, crime_type in enumerate(crime_types):
            option_button = ttk.Button(button_frame, text=crime_type, command=lambda c=category, t=crime_type, v=city_or_year_var: on_button_click(c, t, v))
            option_button.grid(row=1, column=j, pady=5)

    end_button = ttk.Button(root, text="結束", command=lambda: end_program(root))
    end_button.grid(row=len(option_values_crime_type) + 4, column=0, columnspan=4, pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_gui()


