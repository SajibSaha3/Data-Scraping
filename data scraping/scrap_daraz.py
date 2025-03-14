from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import re

driver = webdriver.Chrome()

driver.get("https://www.daraz.com.bd/catalog/?q=sunglasses")# http request sent hoi
driver.maximize_window()

text = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/a').text
print(text)

link = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/a').get_attribute("href")
print(link)


im_new = []
for i in range(1,10):
    j = str(i)
    image = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div['+j+']/div/div/div[1]/div/a/div/img').get_attribute("src")
    im_new.append(image)

print(im_new)





time.sleep(60)# sec
driver.quit()