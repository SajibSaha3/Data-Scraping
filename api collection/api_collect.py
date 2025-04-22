from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Step 1: Set up driver
driver = webdriver.Chrome()

# Step 2: Go to the website
driver.get("https://www.creativeitinstitute.com/")
driver.maximize_window()
time.sleep(5)

# Step 3: Find all top menu items
menu_items = driver.find_elements(By.CSS_SELECTOR, 'nav ul li a')

# Step 4: Extract name and URL
menu_data = []
for item in menu_items:
    text = item.text.strip()
    href = item.get_attribute('href')
    if text and href:
        print(f"{text} --> {href}")
        menu_data.append({
            "Menu Name": text,
            "Menu URL": href
        })

# Step 5: Save to CSV
df = pd.DataFrame(menu_data)
df.to_csv("creativeit_menu_links.csv", index=False, encoding='utf-8-sig')

print("✅ Menu items saved to creativeit_menu_links.csv")
time.sleep(5)
driver.quit()
