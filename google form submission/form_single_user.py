from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()
driver.get('https://www.creativeitinstitute.com/contact-us') # Replace with the actual URL of the form
driver.maximize_window()

name = "sanjida"
email = "sanjida@gmail.com"
phone = "01700000000"
course = "Python Django"
text = "I am interested in the Python Django course. Please contact me for more details."

driver.find_element(By.NAME, 'name').send_keys(name)
time.sleep(2)  # Wait for the page to load
driver.find_element(By.NAME, 'email').send_keys(email)
time.sleep(2)  # Wait for the page to load
driver.find_element(By.NAME, 'phone').send_keys(phone)
time.sleep(2)  # Wait for the page to load
driver.find_element(By.NAME, 'course').send_keys(course)
time.sleep(2)  # Wait for the page to load
driver.find_element(By.NAME, 'text_area').send_keys(text)
time.sleep(5)  # Wait for the page to load
# Click the submit button
submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]')   
submit_button.click()
# Wait for a few seconds to see the result
time.sleep(10)
driver.quit()