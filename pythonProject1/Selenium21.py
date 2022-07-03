#Boostrap DropDown

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#Chrome
serv_obj = Service("C:\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

countriesList = driver.find_elements(By.XPATH,"//select[@id='billing_country']/option")

print(len(countriesList))

for country in countriesList:
    if country.text == 'Turkey':
        country.click()
        break


