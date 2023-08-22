from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import os

# start webdriver and load website from disk
driver = webdriver.Chrome()
url = 'file:///' + os.getcwd() + '/examples/websites/dropdown.html'
driver.get(url)
time.sleep(1)

# select element
select = Select(driver.find_element(By.ID,'country'))
time.sleep(2)

# select by visible text
select.select_by_visible_text('Germany')

time.sleep(2)
# select by value 
select.select_by_value('5')

time.sleep(2)
