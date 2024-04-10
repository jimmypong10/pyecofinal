from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from time import sleep
import glob
import shutil
import os


def crawl(type,URL):
    driver = webdriver.Chrome() 
    driver.get(URL) 
    driver.implicitly_wait(3)
    try:
        download_csv = driver.find_element(By.LINK_TEXT, type)
        download_csv.click()
        try:
            driver.implicitly_wait(3)
            driver.switch_to.frame('frame1')
            driver.switch_to.frame('selframe2')
            select_element = driver.find_element(By.NAME, "outmode")
            select = Select(select_element)
            select.select_by_index(1)
            select_element = driver.find_element(By.NAME, "cycle")
            select = Select(select_element)
            select.select_by_index(0)
            button = driver.find_element(By.NAME, "querybtn")
            button.click()
            sleep(1)
            error = 0
        except NoSuchElementException:
            print('查詢畫面內無法定位')
            error = 1
        """
        except Exception as e:
            print(e)
            """
    except NoSuchElementException:
        print('無法定位')
        error = 1
    driver.close()
    return error
def to_storage(type,download_file):
    list_of_files = glob.glob(download_file+'/*')
    latest_file = max(list_of_files, key=os.path.getctime)
    #print(latest_file)
    if os.path.exists("./temp/file.xlsx"):
        os.remove("./temp/file.xlsx")
    shutil.copyfile(latest_file,"./temp/file.xlsx")
    #下載檔案到這邊的一大塊是把檔案取名字 丟到temp資料夾