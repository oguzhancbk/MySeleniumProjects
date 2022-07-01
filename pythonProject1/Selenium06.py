## Popup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
#driver.get("https://the-internet.herokuapp.com/basic_auth")
#driver.get("https://username:password@test.com")
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()
driver.implicitly_wait(15)
driver.close()

