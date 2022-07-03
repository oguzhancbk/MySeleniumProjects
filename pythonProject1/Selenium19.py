#How to Download File

from selenium import webdriver
from selenium.webdriver.common.by import By
import os
location = os.getcwd()
"""""
def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:\chromedriver.exe")
    #Dosyaları istediğiniz yere indirin
    preferences = {"download.default_directory":location}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",preferences)
    driver = webdriver.Chrome(service=serv_obj,options=ops)
    return driver

"""""

#Pdf_File_Download

def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:\chromedriver.exe")
    #Dosyaları istediğiniz yere indirin
    preferences = {"download.default_directory":location,"plugins.always_open_pdf_externally":True}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",preferences)
    driver = webdriver.Chrome(service=serv_obj,options=ops)
    return driver



#Otomasyon Kod
driver=chrome_setup()
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/")
driver.maximize_window()
driver.find_element(By.XPATH,"//tbody/tr[1]/td[5]/a[1]").click()

