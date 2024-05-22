from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import logging
import time

# Configure logging
logging.basicConfig(filename='appointment_checker.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

# URL of the appointment page
url = 'https://service2.diplo.de/rktermin/extern/choose_categoryList.do?locationCode=isla&realmId=108'

# Keyword to look for
keyword = 'study visa'

# Refresh interval in seconds
refresh_interval = 1

# Path to your WebDriver executable
webdriver_path = r'C:\Users\Omair Ahmad\Downloads\chromedriver-win64\chromedriver.exe'  # Update this path

# Configure WebDriver options
options = Options()
options.add_argument('--headless')  # Run headless Chrome
options.add_argument('--disable-gpu')  # Disable GPU acceleration
options.add_argument('--no-sandbox')  # Bypass OS security model
options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems

# Initialize the WebDriver
service = Service(webdriver_path)
driver = webdriver.Chrome(service=service, options=options)

def check_appointments():
    try:
        driver.get(url)
        time.sleep(5)  # Wait for the page to load completely
        
        page_text = driver.find_element(By.TAG_NAME, 'body').text
        
        # Check if the keyword is in the page
        if keyword.lower() in page_text.lower():
            logging.info('Appointment is available!')
            print('Appointment is available!')
            # Add code here to trigger a notification (e.g., send an email or SMS)
        else:
            logging.info('No appointments available.')
            print('No appointments available.')
    
    except Exception as e:
        logging.error(f'Error fetching the page: {e}')
        print(f'Error fetching the page: {e}')

# Loop to check the page at regular intervals
try:
    while True:
        check_appointments()
        time.sleep(refresh_interval)
finally:
    driver.quit()
