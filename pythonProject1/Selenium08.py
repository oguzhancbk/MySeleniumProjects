#Iframe with in an Iframe

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("http://demo.automationtesting.in/Frames.html")
driver.maximize_window()

driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()
time.sleep(2)
outerframe = driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outerframe)
time.sleep(2)
innerframe = driver.find_element(By.XPATH,"/html[1]/body[1]/section[1]/div[1]/div[1]/iframe[1]")
driver.switch_to.frame(innerframe)
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Welcome")
# driver.switch_to.parent_frame()
