from selenium import webdriver
import time
import os

# start webdriver and load website from disk
driver = webdriver.Firefox()
url = 'file:///' + os.getcwd() + '/websites/textbox.html'
driver.get(url)
time.sleep(1)
 
# enter text
field1 = driver.find_element_by_id("textbox")
field1.send_keys('Selenium example text\nAnother line\nAnother line..')
time.sleep(1)

# close browser
time.sleep(5)
driver.quit()

