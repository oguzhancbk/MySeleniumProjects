# Options , Static WebTable , Dynamic WebTable

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications") #Chrome seleniumu engelliyorsa bunu yap.

serv_obj = Service("C:\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj,options=ops)
driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
driver.maximize_window()

"""""

#STATIC WEBTABLE

#Count number of rows & columns
#Read spesific row & Column data
#Read all the rows & Columns data
#Read data based on condition(List books name whose author is Ozi)

#Count number of rows & columns
rows_count = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
columns_count = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))
print(rows_count) #7
print(columns_count) #4
print("----------------------------------------------------------------\n")

#Read spesific row & Column data
data = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[5]/td[1]")
print(data.text)
print("----------------------------------------------------------------\n")

#Read all the rows & Columns data

for r in range(2,rows_count+1):
    for c in range(1,columns_count+1):
        data = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td["+str(c)+"]").text
        print(data)
    print()

print("----------------------------------------------------------------\n")
#Read data based on condition(List books name whose author is Ozi)

for r in range(2,rows_count+1):
    author_name = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[2]").text
    if author_name == 'Mukesh':
        bookname = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[1]").text
        print(bookname,"    ",author_name)
    print()

"""""

# Dynamic WebTables

login = driver.find_element(By.XPATH,"//input[@id='txtUsername']").send_keys("Admin")
password = driver.find_element(By.XPATH,"//input[@id='txtPassword']").send_keys("admin123")
login_button = driver.find_element(By.XPATH,"//input[@id='btnLogin']").click()
driver.find_element(By.XPATH,"//b[normalize-space()='Admin']").click()

rows_count = len(driver.find_elements(By.XPATH,"//table/tbody/tr"))

count=0
for r in range(1,rows_count+1):
    status = driver.find_element(By.XPATH,"//table[@id='resultTable']/tbody/tr["+str(r)+"]/td[5]").text
    if status == "Enabled":
        count+=1

print("Total rows = ",rows_count)
print("Total enabled count= ",count)
print("Total disabled count= ",rows_count-count)
time.sleep(2)
driver.close()