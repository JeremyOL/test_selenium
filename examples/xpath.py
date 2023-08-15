from selenium import webdriver
import time
import os
from selenium.webdriver.chrome.options import Options

# start webdriver and load website from disk
driver = webdriver.Firefox()
url = 'file:///' + os.getcwd() + '/websites/xpath.html'
driver.get(url)
time.sleep(1)
 
# click button
python_button = driver.find_element_by_xpath("/html/body/form/input[3]")
python_button.click()
time.sleep(1)

python_button = driver.find_element_by_xpath("/html/body/form/input[2]")
python_button.click()
time.sleep(1)

python_button = driver.find_element_by_xpath("/html/body/form/input[1]")
python_button.click()


time.sleep(5)
driver.quit()

