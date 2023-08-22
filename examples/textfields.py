from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# start webdriver and load website from disk
driver = webdriver.Chrome()
url = 'file:///' + os.getcwd() + '/examples/websites/textfields.html'
driver.get(url)
time.sleep(1)
 
# enter username
field1 = driver.find_element(By.ID, "FirstName")
field1.send_keys('Donald')
time.sleep(1)

# enter password
field2 = driver.find_element(By.ID, "LastName")
field2.send_keys('Mouse')
time.sleep(1)

# close browser
time.sleep(5)
driver.quit()

