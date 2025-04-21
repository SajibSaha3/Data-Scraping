from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = Options() # Set up Chrome options if needed ja defult behave ke customise kore 
chrome_options.add_argument(r"--user-data-dir = C:\Users\Sajib\AppData\Local\Google\Chrome\User Data")  # Run in headless mode (no GUI)

chrome_options.add_argument("--profile-directory = Default")  # Use a specific profile (optional)
chrome_options.add_argument("--headless")  # Uncomment this line to run in headless mode
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=chrome_options)
  # Initialize the Chrome driver with options
# Initialize the Chrome driver
driver = webdriver.Chrome()
driver.get("https://www.example.com/form")  # Replace with the actual URL of the form