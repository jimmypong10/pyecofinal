from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
from selenium import webdriver


def Click(button,Xpath,driver):
    element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,Xpath)))
    element.click()
    
def Download (target,URL):
    driver = webdriver.Chrome() 
    driver.get(URL) 
    driver.implicitly_wait(1)
    # 載入網頁
    driver.get(URL)

    # 等待元素時間
    #wait = WebDriverWait(driver, 60)
    driver.implicitly_wait(60)
    
    check = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.LINK_TEXT,target)))
    check.click()
    #進入frame
    iframe=driver.find_element(By.ID,'frame1')
    driver.switch_to.frame(iframe)
    frame1=driver.find_element(By.NAME,'leftframe1')
    driver.switch_to.frame(frame1)
    
    #選擇發破數
    Click('caseNum','/html/body/form/table/tbody/tr[3]/td/a',driver)
    
    #進入frame
    driver.switch_to.parent_frame()  
    frame2=driver.find_element(By.NAME,'selframe2')
    driver.switch_to.frame(frame2)
    
    #選擇破獲率
    Click('detectionRate1','/html/body/form/table[3]/tbody/tr[2]/td[1]/table[1]/tbody/tr/td[2]/font/a',driver)
    Click('detectionRate2','/html/body/form/table[3]/tbody/tr[2]/td[1]/table[4]/tbody/tr/td[2]/input',driver)
    #選擇縣市(全選)
    Click('city','/html/body/form/table[3]/tbody/tr[2]/td[2]/table[1]/tbody/tr/td[2]/font/a',driver)   
    #選擇excel檔
    #找到選擇框
    select_element=driver.find_element(By.ID,"outmode")
    #選擇選擇框
    select=Select(select_element)
    #選擇選擇框內選項-第一個選項
    select.select_by_index(1)
    
       
    #點擊查詢按鈕
    Click('search','/html/body/form/table[1]/tbody/tr/td[1]/input',driver)
    time.sleep(5)
    
    #移至新視窗
#    new_page=target+'破數查詢結果網頁'
#    for page in driver.window_handles:
#        driver.switch_to.window(page)
#        if driver.title==new_page:
#           break
    
    #點擊轉置
#    Click("transpose","/html/body/form/table[1]/tbody/tr[1]/td[4]/input",driver)
    
        
    #點擊下載
#    Click("download","/html/body/form/table[1]/tbody/tr[1]/td[6]/input",driver)
    
    # 關閉瀏覽器
    driver.quit()
    
    



    

    


