from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
import os

# start webdriver and load website from disk
driver = webdriver.Firefox()
url = 'file:///' + os.getcwd() + '/websites/dropdown.html'
driver.get(url)
time.sleep(1)

# select element
select = Select(driver.find_element_by_id('country'))
time.sleep(2)

# select by visible text
select.select_by_visible_text('Germany')

# select by value 
#select.select_by_value('5')
