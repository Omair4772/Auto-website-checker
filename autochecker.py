import requests
from bs4 import BeautifulSoup
import logging
import time

# Configure logging
logging.basicConfig(filename='appointment_checker.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

# URL of the appointment page
url = 'https://google.com/'

# Keyword to look for
keyword = 'google'

# Refresh interval in seconds
refresh_interval = 1

def check_appointments():
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Check if the keyword is in the page
        if keyword in soup.get_text():
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
