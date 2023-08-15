from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import os

# start webdriver and load website from disk
driver = webdriver.Chrome()
url = os.getcwd() + '/examples/websites/button.html'
driver.get(url)
time.sleep(1)

# click button
python_button = driver.find_element(By.XPATH,"//button[contains(text(),'Click Me!')]")
python_button.click()
# close javascript popup
time.sleep(1)
alert = driver.switch_to.alert
alert.accept()

time.sleep(5)
driver.quit()

