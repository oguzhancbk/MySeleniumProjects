#HandleCookies

import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#Chrome
serv_obj = Service("C:\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

#Cookileri yakalıyoruz.
driver.get("https://www.nopcommerce.com/tr/demo")
driver.maximize_window()
cookies = driver.get_cookies()
print("Size of cookies",len(cookies))
#Tüm çerezlerin ayrıntılarını yazdır
for c in cookies:
    print(c.get('name'))

#Tarayıcıya yeni çerez ekle
driver.add_cookie({"name":"MyCookie", "value":"123456"})
cookies=driver.get_cookies()
print("Yeni Cookie sayısı= ",len(cookies))

#Tarayıcıdan belirli çerezi sil
driver.delete_cookie("MyCookie")
cookies=driver.get_cookies()
print(len(cookies))
#Tüm cookieleri sil
driver.delete_all_cookies()
cookies=driver.get_cookies()
print(len(cookies))

time.sleep(2)
driver.quit()