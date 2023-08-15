from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import os

# start webdriver and load website from disk
driver = webdriver.Chrome()
url = os.getcwd() + '/examples/websites/checkbox.html'
driver.get(url)
time.sleep(1)

# select element
cbox = driver.find_element(By.XPATH,'/html/body/form/input[3]')
cbox.click()
time.sleep(2)

# select element
cbox = driver.find_element(By.XPATH,'/html/body/form/input[1]')
cbox.click()
time.sleep(2)

