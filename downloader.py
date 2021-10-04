from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import getpass

driver = webdriver.Chrome('C:\Stuff\Selenium Drivers\chromedriver.exe')
driver.get('https://onq.queensu.ca')

#
#username = 
#password = 

user : WebElement = driver.find_element_by_id('#i0116')
user.send_keys(input("Username: "))
user.send_keys(Keys.RETURN)

passwordInput : WebElement = driver.find_element_by_xpath('/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[2]/div/div[2]/input')
passwordInput.clear()
passwordInput.send_keys(getpass.getpass("Password: "))
passwordInput.send_keys(Keys.RETURN)
