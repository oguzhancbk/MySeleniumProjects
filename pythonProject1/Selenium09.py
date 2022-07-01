#HandleBrowserWindows

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

#Step 1
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
windowsIDs = driver.window_handles

"""""
parentwindowID = windowsIDs[0] ## İlk sekmeye bunu açar
childwindowID = windowsIDs[1] ## İkinci sekmeye bunu açar

print(parentwindowID,childwindowID)

driver.switch_to.window(childwindowID) ## Bunu yaptıktan sonra 1.yi açtıktan sonra buna geçer sonra tekrar ilkine geçer.
print("tittle of the child window",driver.title)
driver.switch_to.window(parentwindowID)
print("ttile of the parent window",driver.title)

"""""

#Step2
"""""
for winID in windowsIDs:
    driver.switch_to.window(winID)
    print(driver.title)
    
"""""

#Step3

for winID in windowsIDs:
    driver.switch_to.window(winID)
    time.sleep(2)
    if driver.title == "OrangeHRM":
        driver.close()