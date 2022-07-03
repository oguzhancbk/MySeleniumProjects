#Drag and drop

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service("C:\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

"""""
roma_ele = driver.find_element(By.XPATH,"//div[@id='box6']")
italy_ele = driver.find_element(By.XPATH,"//div[@id='box106']")
madrid_ele = driver.find_element(By.XPATH,"//div[@id='box7']")
spain_ele = driver.find_element(By.XPATH,"//div[@id='box107']")
wash_ele = driver.find_element(By.XPATH,"//div[@id='box3']")
united_states_ele = driver.find_element(By.XPATH,"//div[@id='box103']")
b = driver.find_element(By.XPATH,"//div[@id='box1']")
b_ele = driver.find_element(By.XPATH,"//div[@id='box101']")
c = driver.find_element(By.XPATH,"//div[@id='box2']")
c_ele = driver.find_element(By.XPATH,"//div[@id='box102']")
d = driver.find_element(By.XPATH,"//div[@id='box4']")
d_ele = driver.find_element(By.XPATH,"//div[@id='box104']")  #1,2,3,4,5,6,7
act = ActionChains(driver)
act.drag_and_drop(roma_ele,italy_ele).perform()
act.drag_and_drop(madrid_ele,spain_ele).perform()
act.drag_and_drop(wash_ele,united_states_ele).perform()
act.drag_and_drop(c,c_ele).perform()
act.drag_and_drop(b,b_ele).perform()
act.drag_and_drop(d,d_ele).perform()

"""""
act = ActionChains(driver)
j = 101
for i in range(1,8):
        a = driver.find_element(By.XPATH,"//div[@id='box"+str(i)+"']")
        a_ele = driver.find_element(By.XPATH,"//div[@id='box"+str(j)+"']")
        act.drag_and_drop(a,a_ele).perform()
        j+=1
        if j == 109:
            break;
time.sleep(2)
driver.close()