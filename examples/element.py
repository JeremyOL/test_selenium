from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# start webdriver and load website from disk
driver = webdriver.Chrome()
url = os.getcwd() + '/examples/websites/element.html'
driver.get(url)
time.sleep(1)
 
# get element text
print( driver.find_element(By.ID, "title1").text )
print( driver.find_element(By.ID, "title2").text )
print( driver.find_element(By.ID, "text1").text )
print( driver.find_element(By.ID, "text2").text )
print( driver.find_element(By.ID, "profile").text )



time.sleep(5)
driver.quit()

