from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# start webdriver and load website from disk
driver = webdriver.Chrome()
url = os.getcwd() + '/examples/websites/links.html'
driver.get(url)
time.sleep(1)

elems = driver.find_elements(by=By.XPATH , value="//a[@href]")
for elem in elems:
    print(elem.get_attribute("href"))
    print(elem.get_attribute("text"))
    
driver.quit()
