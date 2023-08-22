from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# start webdriver and load website from disk
driver = webdriver.Chrome()
url = 'file:///' + os.getcwd() + '/examples/websites/radio.html'
driver.get(url)
time.sleep(1)

# select element
radio = driver.find_element(By.XPATH, '/html/body/form/input[3]')
radio.click()
time.sleep(2)

