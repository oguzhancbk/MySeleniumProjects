#Slider

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service("C:\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

act = ActionChains(driver)

min_slider = driver.find_element(By.XPATH,"//body//div//span[1]")
max_slider = driver.find_element(By.XPATH,"//body//div//span[2]")

print("Önceki lokasyon\n")
print(min_slider.location)
print(max_slider.location)
print("-----------------------\n")
print("Sonraki lokasyon\n")

act.drag_and_drop_by_offset(min_slider,100,0).perform()
act.drag_and_drop_by_offset(max_slider,-39,0).perform()

print(min_slider.location)
print(max_slider.location)