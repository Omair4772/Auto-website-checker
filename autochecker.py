import requests
from bs4 import BeautifulSoup
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

# Headers to mimic a real browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

def check_appointments():
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Check if the keyword is in the page
        if keyword.lower in soup.get_text().lower:
            logging.info('Appointment is available!')
            print('Appointment is available!')
            # Add code here to trigger a notification (e.g., send an email or SMS)
        else:
            logging.info('No appointments available.')
            print('No appointments available.')
    
    except requests.exceptions.RequestException as e:
        logging.error(f'Error fetching the page: {e}')

# Loop to check the page at regular intervals
while True:
    check_appointments()
    time.sleep(refresh_interval)
