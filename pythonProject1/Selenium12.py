"""""
ActionChains

1-) Mouse hover  move_to_element(element)
2-) Right Click  context_click(element)
3-) Double Click dobule_click(element)
4-) Drag and Drop

"""""
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service("C:\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

#Login
login = driver.find_element(By.XPATH,"//input[@id='txtUsername']").send_keys("Admin")
password = driver.find_element(By.XPATH,"//input[@id='txtPassword']").send_keys("admin123")
login_button = driver.find_element(By.XPATH,"//input[@id='btnLogin']").click()

#Admin->User Management->Users
admin = driver.find_element(By.XPATH,"//b[normalize-space()='Admin']")
user_management = driver.find_element(By.XPATH,"//a[@id='menu_admin_UserManagement']")
user = driver.find_element(By.XPATH,"//a[@id='menu_admin_viewSystemUsers']")

#MouseHover

act = ActionChains(driver)

act.move_to_element(admin).move_to_element(user_management).move_to_element(user).click().perform()