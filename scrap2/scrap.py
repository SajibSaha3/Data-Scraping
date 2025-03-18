import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math
# Initialize WebDriver
driver = webdriver.Chrome()
driver.get(f"https://www.daraz.com.bd/catalog/?page=1&q=dress&spm=a2a0e.searchList.search.d_go.51122285dnHamt")
driver.maximize_window()
import re
product_number = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[1]/div/div[1]/div/div/span[1]').text
number = int(re.search(r'\d+', product_number).group())
print(number)
total_pages = math.ceil(number/40)
print('total number of page is', total_pages)

# Lists to store extracted data
list_text = []
link = []
ima_link = []

# Find all product elements           
for page in range(1, total_pages+1):
    p = str(page)
    driver.get(f"https://www.daraz.com.bd/catalog/?page={p}&q=dress&spm=a2a0e.searchList.search.d_go.51122285dnHamt")
    driver.maximize_window()
    products = driver.find_elements(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[*]/div/div')
# Loop through each product and extract text, link, and image
    number_of_product = len(products)
    print(f"Found {number_of_product} products on page {page}")

    # Ensure we take 40 per page, except the last page where we take all available
    for product in products[: min(number_of_product, 40)]:
        try:
            text_element = product.find_element(By.XPATH, './div[2]/div[2]/a')
            image_element = product.find_element(By.XPATH, './div[1]/div/a/div/img')

            list_text.append(text_element.text)
            link.append(text_element.get_attribute("href"))
            ima_link.append(image_element.get_attribute("src"))

        except Exception as e:
            print("Error extracting data for a product:", e)

print("extracted data")
print("Extracted Texts:", list_text)
print()
print("Extracted Links:", link)
print()
print("Extracted Image Links:", ima_link)


time.sleep(60)
driver.quit()

