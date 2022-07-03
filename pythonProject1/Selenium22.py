#CaptureScreenShot

import os
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

driver.get("https://www.nopcommerce.com/tr/demo")
driver.maximize_window()
driver.save_screenshot(os.getcwd()+"\\home2.png")
time.sleep(2)
driver.quit()