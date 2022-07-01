import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)

driver.get("https://itera-qa.azurewebsites.net/home")
driver.maximize_window()
driver.implicitly_wait(15)
time.sleep(2)
test_automation_button = driver.find_element(By.XPATH,"//a[normalize-space()='Test Automation']").click()

name = driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Oguzhan")
mobile_number = driver.find_element(By.XPATH,"//input[@id='phone']").send_keys("5451728585")
email = driver.find_element(By.XPATH,"//input[@id='email']").send_keys("ozi5@gmail.com")
password = driver.find_element(By.XPATH,"//input[@id='password']").send_keys("1234567890a.")
address = driver.find_element(By.XPATH,"//textarea[@id='address']").send_keys("Turkey/Ist")

#CHECKBOX AND RADIOBUTTONS

#checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
#print(len(checkboxes))

#Step1
"""""

for i in range(len(checkboxes)):
    checkboxes[i].click()

#Step2

for chechbox in checkboxes:
    weekname = chechbox.get_attribute('id')
    if weekname == 'monday' or weekname == 'sunday':
        chechbox.click()
#Totalnumberofelements-2=starting index


for i in range(len(checkboxes)-2,len(checkboxes)):
    checkboxes[i].click()
#select first 2 checkbox

for i in range(len(checkboxes)):
    if i<2:
        checkboxes[i].click()
#clearing all the checkboxes
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()
"""""

radiobuttons_gender = driver.find_elements(By.XPATH,"//input[@type='radio' and @class='form-check-input']")

for radio in radiobuttons_gender:
    gender = radio.get_attribute('id')
    if gender == 'male':
        radio.click()

checkboxbuttons_gender = driver.find_elements(By.XPATH,"//input[@type='checkbox' and @class='form-check-input']")

for checkbox in checkboxbuttons_gender:
    gender2 = checkbox.get_attribute('id')
    if gender2 == 'monday' or gender2 == 'saturday':
        checkbox.click()

time.sleep(2)
driver.close()