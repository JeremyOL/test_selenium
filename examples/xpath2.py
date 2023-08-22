from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# start webdriver and load website from disk
driver = webdriver.Chrome()
url = 'file:///' + os.getcwd() + '/examples/websites/example.html'
driver.get(url)
time.sleep(1)
 
# click button
python_button = driver.find_element(By.XPATH, "//*[contains(text(),'Parrot')]")
python_button.click()
time.sleep(1)

time.sleep(5)
driver.quit()

