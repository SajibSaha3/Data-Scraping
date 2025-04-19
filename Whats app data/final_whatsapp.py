from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd
import re

# Launch browser
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
print("Scan QR Code to log in...")
time.sleep(40)  # Wait for QR login manually
driver.maximize_window()

group_name = "Machine and Deep Learning Application-Webinar"

# Search and open the group
search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
search_box.click()
search_box.send_keys(group_name)
time.sleep(5)

group = driver.find_element(By.XPATH, f'//span[@title="{group_name}"]')
group.click()
time.sleep(3)

# Open group info
group_info_btn = driver.find_element(By.XPATH, '//*[@id="main"]/header/div[2]/div[1]/div/span')
group_info_btn.click()
time.sleep(2)

# Scroll to load members
member_panel = driver.find_element(By.XPATH, '//div[@tabindex="-1"]')

seen_members = set()
member_data = []

prev_count = 0
scroll_attempts = 0
max_scrolls = 50

while scroll_attempts < max_scrolls:
    items = driver.find_elements(By.XPATH, '//div[@role="button"]//span[contains(@class,"selectable-text")]')
    for item in items:
        name_or_number = item.text.strip()
        if name_or_number and name_or_number not in seen_members:
            seen_members.add(name_or_number)
            member_data.append({"Name or Number": name_or_number})

    driver.execute_script("arguments[0].scrollTop += 500;", member_panel)
    time.sleep(1.5)

    if len(seen_members) == prev_count:
        scroll_attempts += 1
    else:
        scroll_attempts = 0
        prev_count = len(seen_members)

# Save raw data to CSV first (debugging)
raw_df = pd.DataFrame(member_data)
raw_df.to_csv("raw_whatsapp_data.csv", index=False, encoding="utf-8-sig")
print(f"Raw data saved with {len(member_data)} entries")

# Print some samples for debugging
print("Sample data collected:")
for i, member in enumerate(member_data[:5]):
    print(f"Member {i+1}: {member['Name or Number']}")

# Process data with simpler approach
excel_data = []
for member in member_data:
    info = member["Name or Number"]
    
    # If contains a plus sign and digits, likely a phone number
    if '+' in info and any(c.isdigit() for c in info):
        excel_data.append([info.strip()])
    # Or if mostly digits (>60% of characters)
    elif sum(c.isdigit() for c in info) > len(info) * 0.6:
        excel_data.append([info.strip()])

# Save to Excel
if excel_data:
    excel_df = pd.DataFrame(excel_data, columns=["Phone Number"])
    excel_df.to_excel("whatsapp_group_members.xlsx", index=False)
    print(f"Excel file created with {len(excel_data)} phone numbers")
else:
    print("No phone numbers were extracted!")

# Alternative approach with more aggressive pattern matching
print("Trying alternative extraction method...")
alt_excel_data = []

for member in member_data:
    info = member["Name or Number"]
    
    # Look for any sequence with 8+ digits (likely a phone number)
    if sum(c.isdigit() for c in info) >= 8:
        alt_excel_data.append([info.strip()])
    
    # Also check for embedded numbers with the pattern +XXX
    phone_patterns = [
        r'\+\d+\s*\d+[\d\s\-]+',  # +XXX XXXXX patterns
        r'\d{10,}',               # Any 10+ digit sequence
        r'\d{3,}[\-\s]\d{3,}'     # Patterns like XXX-XXXX
    ]
    
    for pattern in phone_patterns:
        matches = re.findall(pattern, info)
        for match in matches:
            if match.strip() not in [row[0] for row in alt_excel_data]:
                alt_excel_data.append([match.strip()])

# Save alternative results to Excel
if alt_excel_data:
    alt_excel_df = pd.DataFrame(alt_excel_data, columns=["Phone Number"])
    alt_excel_df.to_excel("whatsapp_members_alt.xlsx", index=False)
    print(f"Alternative Excel file created with {len(alt_excel_data)} phone numbers")

time.sleep(3)
driver.quit()