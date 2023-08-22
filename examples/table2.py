from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# start webdriver and load website from disk
driver = webdriver.Chrome()
url = 'file:///' + os.getcwd() + '/examples/websites/table.html'
driver.get(url)
time.sleep(1)

# select table 
table = driver.find_element(By.ID, 'table')

# iterate through table
rows = table.find_elements(By.TAG_NAME, "tr")

# get header rows
headers = rows[0].find_elements(By.TAG_NAME, "th")
for header in headers:
    print(header.text)

# get row
for row in rows:
    if len(row.find_elements(By.TAG_NAME, "td")) > 0:
        col = row.find_elements(By.TAG_NAME, "td")[1]
        print(col.text)

time.sleep(5)
driver.quit()

