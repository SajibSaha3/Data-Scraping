from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome with user profile
chrome_options = Options()
chrome_options.add_argument(r'--user-data-dir=C:\Users\Sajib\AppData\Local\Google\Chrome\User Data')
chrome_options.add_argument("--profile-directory=Default")
# chrome_options.add_argument("--headless")  # Uncomment if you want headless mode

# Launch browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Open the Google Form
driver.get("https://forms.gle/EPha1tUVgkybtraS8")
driver.maximize_window()
time.sleep(5)  # Let the form load

try:
    # Fill out the first input field
    
    text_input_1 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    # driver.refresh()
    text_input_1.send_keys("Sajib")
    time.sleep(2)
    # radio button selection
    # radio_male = driver.find_element(By.XPATH, '//div[@data-value="Female"]')
    # radio_male.click()
    # time.sleep(2)

    radio_button = '//*[contains(@aria-label, "Male")]'
    try:
        radio_button_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, radio_button))
        )
        actions = ActionChains(driver)
        actions.move_to_element(radio_button_element).click().perform()
        print("Radio button clicked successfully!")
    except Exception as e:
        print("Error clicking radio button:", e)

    # Fill out the second input field
    text_input_2 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    text_input_2.send_keys(20)
    time.sleep(2)

    # Click the submit button
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit_button.click()
    print("Form submitted successfully!")

except Exception as e:
    print("Error:", e)

time.sleep(5)




driver.quit()
