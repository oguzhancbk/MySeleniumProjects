## ALERTS

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
driver.implicitly_wait(15)

driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(2)

alertwindow = driver.switch_to.alert
print(alertwindow.text)
time.sleep(2)
alertwindow.send_keys("welcome")
time.sleep(2)
alertwindow.accept()  # ok button
# alertwindow.dismiss() # cancel button
time.sleep(2)
driver.close()