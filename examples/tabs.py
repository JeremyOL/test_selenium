from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# start webdriver and load website from disk
driver = webdriver.Chrome()
url = 'file:///' + os.getcwd() + '/examples/websites/button.html'
driver.get(url)
time.sleep(1)

# new tab
driver.execute_script('''window.open("http://stackoverflow.com","_blank");''')

# switch tab
time.sleep(1)
driver.switch_to.window(driver.window_handles[0])

# switch tab
time.sleep(1)
driver.switch_to.window(driver.window_handles[1])


time.sleep(5)
driver.quit()

