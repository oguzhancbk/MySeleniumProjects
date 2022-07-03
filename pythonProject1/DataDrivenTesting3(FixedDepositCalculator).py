import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import XLUtils

#Chrome
serv_obj = Service("C:\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()
driver.find_element(By.ID,"wzrk-cancel").click()

file = r"C:\Users\oguzh\PycharmProjects\pythonProject1\caldata.xlsx"
rows = XLUtils.getRowCount(file,"Sheet1")

for r in range(2,rows+1):
    pric = XLUtils.readData(file,"Sheet1",r,1)
    rateOfinterest = XLUtils.readData(file,"Sheet1",r,2)
    per1 = XLUtils.readData(file,"Sheet1",r,3)
    per2 = XLUtils.readData(file, "Sheet1", r, 4)
    fre = XLUtils.readData(file,"Sheet1",r,5)
    exp_mvalue = XLUtils.readData(file, "Sheet1", r, 6)

    driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(pric)
    driver.find_element(By.XPATH,"//input[@id='interest']").send_keys(rateOfinterest)
    driver.find_element(By.XPATH,"//input[@id='tenure']").send_keys(per1)
    periodDrop = Select(driver.find_element(By.XPATH,"//select[@id='tenurePeriod']"))
    periodDrop.select_by_visible_text(per2)
    freDrop = Select(driver.find_element(By.XPATH,"//select[@id='frequency']"))
    freDrop.select_by_visible_text(fre)
    driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[1]/img").click()
    act_mvalue = driver.find_element(By.XPATH,"//span[@id='resp_matval']").text

    if float(exp_mvalue) == float(act_mvalue):
        print("Test passed")
        XLUtils.writeData(file,"Sheet1",r,8,"Passed")
        XLUtils.fillGreenColor(file,"Sheet1",r,8)
    else:
        print("Test failed")
        XLUtils.writeData(file, "Sheet1", r, 8,"Failed")
        XLUtils.fillRedColor(file,"Sheet1",r,8)

    driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[2]/img").click()
    time.sleep(2)

driver.close()
