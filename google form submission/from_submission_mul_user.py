users = [
    ("sanjida", "sanjida@gmail.com", "01700000000", "Python Django", "I am interested in the Python Django course. Please contact me for more details."),
    ("rakib", "rakib@yahoo.com", "01711111111", "Motion Graphics", "Looking forward to learning Motion Graphics. Kindly reach out with more info."),
    ("nazia", "nazia@hotmail.com", "01722222222", "UX/UI Design", "Interested in the UX/UI Design course. Need more details, please."),
    ("tamim", "tamim@outlook.com", "01733333333", "Adobe Photoshop", "Want to join the Adobe Photoshop course. Please provide more information."),
    ("mim", "mim@gmail.com", "01744444444", "Adobe Illustrator", "I'm curious about the Adobe Illustrator course. Can you share more?")
]
users = [
    ("sanjida", "sanjida@gmail.com", "01700000000", "Python Django", "I am interested in the Python Django course. Please contact me for more details."),
    ("rakib", "rakib@yahoo.com", "01711111111", "Motion Graphics", "Looking forward to learning Motion Graphics. Kindly reach out with more info."),
    ("nazia", "nazia@hotmail.com", "01722222222", "UX/UI Design", "Interested in the UX/UI Design course. Need more details, please."),
    ("tamim", "tamim@outlook.com", "01733333333", "Adobe Photoshop", "Want to join the Adobe Photoshop course. Please provide more information."),
    ("mim", "mim@gmail.com", "01744444444", "Adobe Illustrator", "I'm curious about the Adobe Illustrator course. Can you share more?")
]

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get('https://www.creativeitinstitute.com/contact-us') # Replace with the actual URL of the form
driver.maximize_window()    
time.sleep(2)  # Wait for the page to load  





time.sleep(2)  # Wait for the page to load
driver.quit()
