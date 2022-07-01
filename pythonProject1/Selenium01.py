import time

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj=Service("C:\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10) # seconds

#driver.get("https://www.nopcommerce.com/tr/demo")

## Aplication Commands
"""
print(driver.title)  #OrangeHRM
print(driver.current_url) #https://opensource-demo.orangehrmlive.com/
print(driver.page_source) # Python kodları sayfa kaynak kodu
"""
## Conditional commands

#is.display()
#driver.get("https://www.automationexercise.com/")
"""""
visibile = driver.find_element(By.XPATH,"//img[@alt='Website for automation practice']")
print(visibile.is_displayed())
print(visibile.is_enabled())
visible2 = driver.find_element(By.XPATH,"//h2[normalize-space()='Features Items']")
print(visible2.is_enabled())
otorum_ac = driver.find_element(By.XPATH,"//a[normalize-space()='Signup / Login']").click()
visibile3 = driver.find_element(By.XPATH,"//h2[normalize-space()='New User Signup!']")
print(visibile3.is_displayed())
3name = driver.find_element(By.XPATH,"//input[@placeholder='Name']").send_keys("ozi")
"""""
#email = driver.find_element(By.XPATH,"//input[@data-qa='signup-email']").send_keys("ozi5@gmail.com")
#signup = driver.find_element(By.XPATH,"//button[normalize-space()='Signup']").click()
#mr = driver.find_element(By.XPATH,"//input[@id='id_gender1']")
#mr.click()
#mrs = driver.find_element(By.XPATH,"//input[@id='id_gender2']")
#is.selected()
#print(mr.is_selected())
#print(mrs.is_selected())
#link = driver.find_element(By.LINK_TEXT,"Video Tutorials")

#Kaç saniyede sonra yapacağını gösterir.
#time.sleep(5)

#print("Link is= ",link.is_displayed())

#Navigational Commands

#back()
#forward()
#refresh()

#Ekrandaki tüm elementlerin isminlerini yazdır.

#elements = driver.find_elements(By.XPATH,"//ul[@class='nav navbar-nav']")
#for ele in elements:
#    print(ele.text)

## WAIT COMMANDS

#time.sleep(time)
#impclit wait
#explicit wait

driver.get("https://www.google.com")
driver.maximize_window()
searchbox = driver.find_element(By.XPATH,"//input[@title='Ara']")
searchbox.send_keys("Selenium")
searchbox.submit()
mywait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException,
                                                     Exception]
                       )
searchlink = mywait.until(EC.element_to_be_clickable((By.XPATH,"//h3[normalize-space()='Selenium']")))
searchlink.click()

driver.close()