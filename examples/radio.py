from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
import os

# start webdriver and load website from disk
driver = webdriver.Firefox()
url = 'file:///' + os.getcwd() + '/websites/radio.html'
driver.get(url)
time.sleep(1)

# select element
radio = driver.find_element_by_xpath('/html/body/form/input[3]')
radio.click()
time.sleep(2)

