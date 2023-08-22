from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.chrome.options import Options

# start webdriver and load website from disk
driver = webdriver.Chrome()
url = 'file:///' + os.getcwd() + '/examples/websites/xpath.html'
driver.get(url)
time.sleep(1)
 
# click button
python_button = driver.find_element(By.XPATH, "/html/body/form/input[3]")
python_button.click()
time.sleep(1)

python_button = driver.find_element(By.XPATH, "/html/body/form/input[2]")
python_button.click()
time.sleep(1)

python_button = driver.find_element(By.XPATH, "/html/body/form/input[1]")
python_button.click()


time.sleep(5)
driver.quit()

