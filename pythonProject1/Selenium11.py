#DataPicker

#1)Standard
#2)Non-Standard(Customized)


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service("C:\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

"""""

driver.get("https://jqueryui.com/datepicker/")
driver.switch_to.frame(0)

#driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("07/01/2022")

driver.find_element(By.XPATH,"//input[@id='datepicker']").click()

year = "2000"
month = "February"
date = "22"

while True:
    mon = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr =  driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

    if mon == month and yr == year:
        break;
    else:
        #driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click() #Next
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-w']").click() #Previous


days = driver.find_elements(By.XPATH,"//div[@id='ui-datepicker-div']/table/tbody/tr/td/a")

for ele in days:
    if ele.text == date:
        ele.click()
        break
        

"""""

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@id='dob']").click() # opens date picker

datapicker_month = Select(driver.find_element(By.XPATH,"//select[@data-handler='selectMonth']"))
datapicker_month.select_by_visible_text("Feb")

datapicker_year = Select(driver.find_element(By.XPATH,"//select[@data-handler='selectYear']"))
datapicker_year.select_by_visible_text("2000")

alldates = driver.find_elements(By.XPATH,"//div[@id='ui-datepicker-div']/table/tbody/tr/td/a")

for date in alldates:
    if date.text == "22":
        date.click()
        break