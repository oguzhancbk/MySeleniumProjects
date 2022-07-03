#Scrolling

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service("C:\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

act = ActionChains(driver)

#Sayfayı pixel aşağı kaydırme
"""
driver.execute_script("window.scrollBy(0,3000)","")
value = driver.execute_script("return window.pageYOffset;")
print(value)
#Elemanlar görünene kadar sayfayı aşağı kaydırın
flag = driver.find_element(By.XPATH,"//img[@alt='Flag of Turkey']")
driver.execute_script("arguments[0].scrollIntoView();",flag)
value = driver.execute_script("return window.pageYOffset;")
print(value)
"""
#Sayfayı sonuna kadar aşağı kaydır
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print(value)
time.sleep(2)

#Başlangıç ​​pozisyonuna kadar yukarı kaydır
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print(value)
time.sleep(2)
driver.close()
