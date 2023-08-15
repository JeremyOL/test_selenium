from selenium import webdriver
import time
import os

# start webdriver and load website from disk
driver = webdriver.Firefox()
url = 'file:///' + os.getcwd() + '/websites/textfields.html'
driver.get(url)
time.sleep(1)
 
# enter username
field1 = driver.find_element_by_id("FirstName")
field1.send_keys('Donald')
time.sleep(1)

# enter password
field2 = driver.find_element_by_id("LastName")
field2.send_keys('Mouse')
time.sleep(1)

# close browser
time.sleep(5)
driver.quit()

