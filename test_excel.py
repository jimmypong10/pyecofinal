# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 02:08:44 2023

@author: user
"""
import xlwings as xw

def processing ():
    path="./temp/file.xlsx"
    #打該excel並且可看見
    app=xw.App(visible=True , add_book=False)
    #在excel中打開檔案
    ap=app.books.open(path)
    #儲存檔案
    ap.save()
    #關閉檔案
    #ap.close()
    #關閉excel
    app.quit()