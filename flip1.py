# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 23:04:26 2023

@author: user
"""
import os
import pandas as pd
import openpyxl

#找到最新檔案並重新命名
import shutil

def rename(download_folder):
    temp_dir = "./temp"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    if os.path.exists(os.path.join(temp_dir, "file.xlsx")):
        os.remove(os.path.join(temp_dir, "file.xlsx"))

    # 確保下載文件夾不是空的
    if not os.listdir(download_folder):
        raise ValueError("下載文件夾是空的")

    file_lists = [f for f in os.listdir(download_folder) if f.endswith('.xlsx')]
    file_lists.sort(key=lambda fn: os.path.getmtime(os.path.join(download_folder, fn)))

    old_path = os.path.join(download_folder, file_lists[-1])
    new_path = os.path.join(temp_dir, "file.xlsx")

    shutil.move(old_path, new_path)
    return new_path
def transpose(path):
    #轉置
    file=openpyxl(path,header=None).T
    return file

#擷取需要的部分放入新檔案
def retrieve(path, new_file_path):
    file = pd.read_excel(path, header=None).T
    extracted_data = file.iloc[:, 3:5]
    extracted_data.to_excel(new_file_path, index=False)
    new_file = pd.read_excel(new_file_path)
    return new_file