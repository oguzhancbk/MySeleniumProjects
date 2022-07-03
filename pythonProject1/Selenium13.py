#RightClick

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service("C:\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

right_click_me_button = driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")

act = ActionChains(driver)

act.context_click(right_click_me_button).perform() #Right Click
driver.find_element(By.XPATH,"//li[@class='context-menu-item context-menu-icon context-menu-icon-copy context-menu-visible']").click()
driver.switch_to.alert.accept()