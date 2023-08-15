from selenium import webdriver
import time
import os

# start webdriver and load website from disk
driver = webdriver.Firefox()
url = 'file:///' + os.getcwd() + '/websites/example.html'
driver.get(url)
time.sleep(1)
 
# click button
python_button = driver.find_element_by_xpath("//*[contains(text(),'Parrot')]")
python_button.click()
time.sleep(1)

time.sleep(5)
driver.quit()

