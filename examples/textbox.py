from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# start webdriver and load website from disk
driver = webdriver.Chrome()
url = 'file:///' + os.getcwd() + '/examples/websites/textbox.html'
driver.get(url)
time.sleep(1)
 
# enter text
field1 = driver.find_element(By.ID, "textbox")
field1.send_keys('Selenium example text\nAnother line\nAnother line..')
time.sleep(1)

# close browser
time.sleep(5)
driver.quit()

