# utilities/setup.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def initialize_driver():
    """Initialize the WebDriver."""
    driver = webdriver.Chrome()  # You can replace this with another driver if needed
    driver.implicitly_wait(10)  # Implicit wait to handle loading time
    return driver
