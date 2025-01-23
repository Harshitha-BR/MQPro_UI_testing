import time

import pytest
from utilities.readproperties import ReadConfig
from utilities.utils import get_org_passcode_data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



LOGIN_URL = ReadConfig.geturl()  # Get the login URL from the login section
PASSCODE = ReadConfig.get_password()
print(f"Login URL: {LOGIN_URL}, Username:  ")# Get the password for login

@pytest.fixture(scope="function")
def setup():
    # Initialize WebDriver (using Chrome in this example)
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  # Implicit wait to handle loading time
    driver.get(LOGIN_URL)
    yield driver
    driver.quit()


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

def test_passcode_fields_present(setup):
    driver = setup

    # Locate all passcode fields (OTP inputs)
    passcode_fields = driver.find_elements(By.CSS_SELECTOR, 'div.otp-inputGroup .otp-box ion-input')

    # Check if there are exactly 6 passcode fields
    assert len(passcode_fields) == 6, f"The login page does not have 6 passcode fields, found {len(passcode_fields)}"

def test_login_button_disabled(setup):
    driver = setup

    # Locate the login button
    login_button = driver.find_element(By.XPATH, "//app-submit[@buttonText='LOGIN']")

    # Assert that the login button is initially disabled by checking the 'disabled' class
    assert login_button.get_attribute("disabled") is not True, "Login button is not disabled initially"

def test_passcode_input_acceptance(setup):
    driver = setup
    passcode_fields = driver.find_elements(By.XPATH, "//input[@maxlength='1']")

    for i, field in enumerate(passcode_fields):
        field.clear()
        field.send_keys(PASSCODE[i])

def test_unsuccessful_login_with_incorrect_passcode(setup):
    # Scenario 2: Unsuccessful Login with Incorrect Passcode
    driver = setup
    incorrect_code = "2123456"  # Replace with your test OTP code
    passcode_fields = driver.find_elements(By.XPATH, "//input[@maxlength='1']")

    for i, field in enumerate(passcode_fields):
        field.clear()
        field.send_keys(incorrect_code[i])
    login_button = driver.find_element(By.XPATH, "//app-submit[@buttonText='LOGIN']")
    login_button.click()

    # Wait for error message to appear
    error_message_container = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "error-message"))
    )

    # Verify that the error message container is displayed
    assert error_message_container.is_displayed(), "Error message for incorrect passcode not displayed"


def test_invalid_org_id_alert_and_redirect(setup):
    driver = setup

    # Set an invalid org_id and try to access the page
    invalid_org_id = "998"  # Invalid org_id
    url = f"{LOGIN_URL}?org_id={invalid_org_id}"  # Concatenate org_id to the base URL

    # Navigate to the page with the specific invalid org_id
    driver.get(url)

    # Ensure we are on the correct page with the invalid org_id
    assert f"org_id={invalid_org_id}" in driver.current_url, f"URL did not contain org_id={invalid_org_id}"

    # Wait for the alert popup to appear
    time.sleep(2)  # You can replace this with WebDriverWait if needed

    # Check if the alert popup with id 'ion-overlay-1' is present
    try:
        alert_popup = driver.find_element(By.ID, "ion-overlay-1")
        assert alert_popup.is_displayed(), "Alert popup with ID 'ion-overlay-1' is not displayed"
        print("Alert popup appeared as expected.")
    except Exception as e:
        pytest.fail(f"Error: Alert popup not found. Exception: {str(e)}")

    # Locate the close button in the alert popup. (This assumes the button has text 'Close')
    # Adjust this selector based on how the close button is rendered in your application.
    close_button = driver.find_element(By.CLASS_NAME, "alert-button")

    # Click the close button on the alert
    close_button.click()

    # Wait for the page to redirect to the base URL after the alert is closed
    time.sleep(2)  # Optionally, use WebDriverWait to wait for the URL to change

    # Verify that the page has been redirected to the base URL (without org_id)
    assert driver.current_url == LOGIN_URL, f"Page was not redirected to the base URL. Current URL is: {driver.current_url}"

@pytest.mark.parametrize("data", get_org_passcode_data())
def test_passcode_input_with_org_id_and_passcode(setup, data,expected_error="Invalid passcode"):
    """
    This test case will run for each org_id and passcode pair from the `get_org_passcode_data` function.
    """

    driver =setup

    org_id = data["org_id"]
    valid_passcode = data["passcode"]
    url = f"{LOGIN_URL}?org_id={org_id}"

    # Navigate to the page with the specific org_id
    driver.get(url)

    # Ensure we are on the correct page with the org_id in the URL
    assert f"org_id={org_id}" in driver.current_url, f"URL did not contain org_id={org_id}"

    # Wait for the passcode input field to be present
    passcode_fields = driver.find_elements(By.CSS_SELECTOR, 'div.otp-inputGroup .otp-box ion-input')

    # Enter the passcode into the OTP fields and submit
    for i, passcode_field in enumerate(passcode_fields):
        # Get the actual <input> element inside the <ion-input>
        input_element = passcode_field.find_element(By.CSS_SELECTOR, 'input')

        # Send the corresponding digit from the passcode to each input field
        input_element.send_keys(valid_passcode[i])

    login_button = driver.find_element(By.XPATH, "//app-submit[@buttonText='LOGIN']")
    login_button.click()

    try:
        # Check if the error message is displayed (invalid passcode scenario)
        error_message_container = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "error-message"))
        )
        assert error_message_container.text == expected_error, f"Expected error message: '{expected_error}', but got: '{error_message_container.text}'"

    except Exception as e:
        assert "login success"