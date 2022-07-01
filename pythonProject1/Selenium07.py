## Frames

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
#driver.get("https://the-internet.herokuapp.com/basic_auth")
#driver.get("https://username:password@test.com")
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.maximize_window()

driver.switch_to.frame("packageListFrame")
driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()
driver.switch_to.default_content()
driver.switch_to.frame("packageFrame")
driver.find_element(By.LINK_TEXT,"WebDriver").click()
driver.switch_to.default_content()
driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH,"//div[@class='topNav']//a[normalize-space()='Help']").click()
driver.close()