#KeyboardActions

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
driver.get("https://text-compare.com/")
driver.maximize_window()

inptu1 = driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
input2 = driver.find_element(By.XPATH,"//textarea[@id='inputText2']")

inptu1.send_keys("Welcome to Selenium")

act = ActionChains(driver)

#Input1 -> CTRL+A
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
#Input1 -> CTRL+C
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
#Press to Tab
act.send_keys(Keys.TAB).perform()
#Input2 -> CTRL+V
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

#Close
time.sleep(2)
driver.close()
