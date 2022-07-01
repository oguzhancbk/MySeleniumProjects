from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service("C:\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.opencart.com/index.php?route=common/home")
driver.maximize_window()
driver.implicitly_wait(15)

#Dropdown

register = driver.find_element(By.XPATH,"//a[@class='btn btn-black navbar-btn']").click()
username = driver.find_element(By.XPATH,"//input[@id='input-username']").send_keys("ozi123")
firstname = driver.find_element(By.XPATH,"//input[@id='input-firstname']").send_keys("Oguzhan")
lastname = driver.find_element(By.XPATH,"//input[@id='input-lastname']").send_keys("Cbk")
email = driver.find_element(By.XPATH,"//input[@id='input-email']").send_keys("Ozi123@gmail.com")

dropdown=Select(driver.find_element(By.XPATH,"//select[@id='input-country']"))

dropdown.select_by_visible_text("Turkey")

##Capture all the options and print them
alloptions = dropdown.options
print("Total number of options: ",len(alloptions))

for opt in alloptions:
    print(opt.text)

password = driver.find_element(By.XPATH,"//input[@id='input-password']").send_keys("12345")

driver.close()