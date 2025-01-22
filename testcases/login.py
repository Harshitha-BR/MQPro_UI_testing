import time

import pytest
from utilities.readproperties import ReadConfig
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



LOGIN_URL = ReadConfig.geturl()  # Get the login URL from the login section
PASSWORD = ReadConfig.getpassword()
print(f"Login URL: {LOGIN_URL}, Username:  ")# Get the password for login

@pytest.fixture(scope="function")
def setup():
    # Initialize WebDriver (using Chrome in this example)
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  # Implicit wait to handle loading time
    driver.get(LOGIN_URL)
    yield driver
    driver.quit()  # Close browser after test

def test_login_page_elements(setup):
    driver = setup

    # Wait for the login page to load (using explicit waits for better reliability)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Check if the logo is present
    try:
        logo = driver.find_element(By.XPATH, "//img[@alt='Mq Title Logo']")  # Update with the actual XPath or selector for the logo
        assert logo.is_displayed(), "Logo is not displayed"
    except Exception as e:
        assert False, f"Logo not found: {e}"

    # Check if the welcome text is present
    try:
        welcome_text = driver.find_element(By.XPATH, "//h2[contains(text(), 'Welcome to')]")  # Update with actual XPath or selector for welcome text
        assert welcome_text.is_displayed(), "Welcome text is not displayed"
    except Exception as e:
        assert False, f"Welcome text not found: {e}"

    # Check if the passcode fields are present
    try:
        passcode_field = driver.find_element(By.CLASS_NAME, "otp-inputGroup")  # Update with actual field ID or selector
        assert passcode_field.is_displayed(), "Passcode field is not visible"
    except Exception as e:
        assert False, f"Passcode field not found: {e}"

    # Check if the login button is present
    try:
        login_button = driver.find_element(By.XPATH, "//app-submit[@buttonText='LOGIN']")
  # Update with actual button ID or selector
        assert login_button.is_displayed(), "Login button is not visible"
    except Exception as e:
        assert False, f"Login button not found: {e}"

    # Optionally, you can assert the title of the page to make sure it's the login page
    assert "MQ PRO" in driver.title, "Login page did not load correctly"

    # Sleep for a moment to observe (optional)
    time.sleep(2)