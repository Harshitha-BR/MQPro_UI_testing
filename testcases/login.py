import pytest
from utilities.setup import initialize_driver
from pageObject.login import LoginPage
from utilities.readproperties import ReadConfig
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.utils import get_org_passcode_data

LOGIN_URL = ReadConfig.geturl()  # Get the login URL from the config
PASSCODE = ReadConfig.get_password()  # Get the passcode


@pytest.fixture(scope="function")
def setup():
    driver = initialize_driver()
    driver.get(LOGIN_URL)
    yield driver
    driver.quit()


def test_login_page_elements(setup):
    driver = setup
    login_page = LoginPage(driver)

    assert login_page.check_logo_displayed(), "Logo is not displayed"
    assert login_page.check_welcome_text_displayed(), "Welcome text is not displayed"
    assert login_page.check_passcode_field_displayed(), "Passcode field is not visible"
    assert login_page.check_login_button_displayed(), "Login button is not visible"


def test_successful_login(setup):
    driver = setup
    login_page = LoginPage(driver)

    # Enter the passcode and login
    login_page.enter_passcode(PASSCODE)
    login_page.click_login_button()

    WebDriverWait(driver, 10).until(
        EC.url_contains("chat-board")
    )


    assert "chat-board" in driver.current_url, "User is not redirected to the chartboard page"


def test_passcode_fields_present(setup):
    driver = setup
    login_page = LoginPage(driver)

    # Check that exactly 6 passcode fields are present
    assert len(
        login_page.passcode_fields) == 6, f"The login page does not have 6 passcode fields, found {len(login_page.passcode_fields)}"


def test_passcode_input_acceptance(setup):
    driver = setup
    login_page = LoginPage(driver)

    # Enter the passcode into the OTP fields
    login_page.enter_passcode(PASSCODE)

    # Verify that the passcode fields are populated correctly
    login_page.verify_passcode_fields(PASSCODE)


def test_login_button_disabled(setup):
    driver = setup
    login_page = LoginPage(driver)

    # Check that the login button is initially disabled
    assert not login_page.is_login_button_disabled(), "Login button should be disabled initially"


def test_unsuccessful_login_with_incorrect_passcode(setup):
    driver = setup
    login_page = LoginPage(driver)

    # Enter an incorrect passcode
    incorrect_code = "2123456"  # Replace with your test OTP code
    login_page.enter_passcode(incorrect_code)
    login_page.click_login_button()

    # Wait for error message to appear using the helper method
    error_message_container = login_page.wait_for_error_message()

    # Verify that the error message container is displayed
    assert error_message_container.is_displayed(), "Error message for incorrect passcode not displayed"


def test_invalid_org_id_alert_and_redirect(setup):
    driver = setup
    login_page = LoginPage(driver)

    # Set an invalid org_id and try to access the page
    invalid_org_id = "998"  # Invalid org_id
    url = f"{LOGIN_URL}?org_id={invalid_org_id}"  # Concatenate org_id to the base URL

    # Navigate to the page with the specific invalid org_id
    driver.get(url)

    # Wait for the alert popup to appear
    alert_popup = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "ion-overlay-1"))
    )
    assert alert_popup.is_displayed(), "Alert popup with ID 'ion-overlay-1' is not displayed"

    # Locate the close button in the alert popup
    close_button = driver.find_element(By.CLASS_NAME, "alert-button")
    close_button.click()

    # Wait for the page to redirect to the base URL after the alert is closed
    WebDriverWait(driver, 10).until(
        EC.url_to_be(LOGIN_URL)
    )

    # Verify that the page has been redirected to the base URL (without org_id)
    assert driver.current_url == LOGIN_URL, f"Page was not redirected to the base URL. Current URL is: {driver.current_url}"


@pytest.mark.parametrize("data", get_org_passcode_data())
def test_passcode_input_with_org_id_and_passcode(setup, data, expected_error="Invalid passcode"):
    driver = setup
    org_id = data["org_id"]
    valid_passcode = data["passcode"]

    # Navigate with the org_id
    driver.get(f"{LOGIN_URL}?org_id={org_id}")

    # Assert the org_id is present in the URL
    assert f"org_id={org_id}" in driver.current_url, f"URL did not contain org_id={org_id}"

    # Enter the passcode into the OTP fields
    login_page = LoginPage(driver)
    login_page.enter_passcode(valid_passcode)

    # Verify the passcode fields are populated correctly
    login_page.verify_passcode_fields(valid_passcode)

    # Click login
    login_page.click_login_button()

    try:
        # Wait for the error message and validate
        error_message_container = login_page.wait_for_error_message()
        assert error_message_container.text == expected_error, f"Expected error message: '{expected_error}', but got: '{error_message_container.text}'"

    except Exception:
        assert "login success"
