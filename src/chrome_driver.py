from config import config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def start ():
    """
    Configures and starts a Selenium Chrome WebDriver.
    """
    # Set up Chrome options.
    options = Options()
    options.add_argument(f"--user-data-dir={config['user-data-dir']}")
    options.add_argument(f"profile-directory={config['profile-directory']}")

    # Set up Chrome driver service.
    service = Service(config['driver-path'])

    # Launch Chrome.
    return webdriver.Chrome(service=service, options=options)

