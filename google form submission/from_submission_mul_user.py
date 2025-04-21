from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Sample user data
users = [
    ("sanjida", "sanjida@gmail.com", "01700000000", "Python Django", "I am interested in the Python Django course. Please contact me for more details."),
    ("rakib", "rakib@yahoo.com", "01711111111", "Motion Graphics", "Looking forward to learning Motion Graphics. Kindly reach out with more info."),
    ("nazia", "nazia@hotmail.com", "01722222222", "UX/UI Design", "Interested in the UX/UI Design course. Need more details, please."),
    ("tamim", "tamim@outlook.com", "01733333333", "Adobe Photoshop", "Want to join the Adobe Photoshop course. Please provide more information."),
    ("mim", "mim@gmail.com", "01744444444", "Adobe Illustrator", "I'm curious about the Adobe Illustrator course. Can you share more?")
]

# Start browser
driver = webdriver.Chrome()
driver.get('https://www.creativeitinstitute.com/contact-us')
driver.maximize_window()
wait = WebDriverWait(driver, 10)
time.sleep(3)  # Allow page to load initially

# Loop through each user
for i, (name, email, phone, course, text) in enumerate(users, start=1):
    print(f"\n--- Submitting for user {i}: {name} ---")

    # Wait and find form fields
    name_input = wait.until(EC.presence_of_element_located((By.NAME, 'name')))
    email_input = driver.find_element(By.NAME, 'email')
    phone_input = driver.find_element(By.NAME, 'phone')
    course_input = driver.find_element(By.NAME, 'course')
    text_area = driver.find_element(By.NAME, 'text_area')

    # Fill out the form
    name_input.send_keys(name)
    email_input.send_keys(email)
    phone_input.send_keys(phone)
    course_input.send_keys(course)
    text_area.send_keys(text)

    time.sleep(2)

    # Wait until submit button is clickable and scroll into view
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    time.sleep(1)

    # Use JS click to avoid click interception issue
    driver.execute_script("arguments[0].click();", submit_button)

    print(f"✅ Form submitted for {name}")
    time.sleep(4)  # Wait for the form to process

    # Refresh page for the next input
    driver.refresh()
    time.sleep(3)  # Let page reload

# Close browser
driver.quit()

