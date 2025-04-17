import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Open the page
driver.get('https://www.daraz.com.bd/products/2023-i465829987-s2238309140.html')
driver.refresh()
driver.maximize_window()

# Scroll down to load comments
height = driver.execute_script('return document.body.scrollHeight')
print("Total page height:", height)

for i in range(0, height + 550, 50):
    driver.execute_script(f'window.scrollTo(0,{i});')
    time.sleep(0.5)


time.sleep(3)

try:
    comments = driver.find_elements(By.CLASS_NAME, 'content')  
    print(f"Total comments found: {len(comments)}")

    for idx, comment in enumerate(comments, 1):
        print(f"{idx}. {comment.text.strip()}")

except Exception as e:
    print("Error finding comments:", e)

# Keep browser open for inspection
time.sleep(60)
driver.quit()
