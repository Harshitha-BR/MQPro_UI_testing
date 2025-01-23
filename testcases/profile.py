import pytest
from utilities.readproperties import ReadConfig
from utilities.utils import get_org_passcode_data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


LOGIN_URL = ReadConfig.geturl()  # Get the login URL from the login section
PASSCODE = ReadConfig.get_password()
CHAT_URL = "https://sandbox.mqpro.tibilsolutions.com/chat-board"

@pytest.fixture(scope="function")
def setup():
    # Initialize WebDriver (using Chrome in this example)
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  # Implicit wait to handle loading time
    driver.get(LOGIN_URL)
    passcode_fields = driver.find_elements(By.XPATH, "//input[@maxlength='1']")

    for i, field in enumerate(passcode_fields):
        field.clear()
        field.send_keys(PASSCODE[i])
    login_button = driver.find_element(By.XPATH, "//app-submit[@buttonText='LOGIN']")
    login_button.click()

    yield driver
    driver.quit()


def test_profile_icon_present(setup,):
    driver=setup

    profile_icon = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "logo-container"))
    )

    assert profile_icon.is_displayed(), "profile image is not visible"

    profile_icon.click()
    profile_settings_menu = driver.find_element(By.CLASS_NAME, "mat-mdc-menu-panel")
    assert profile_settings_menu.is_displayed(), "Profile Settings menu is not visible"

    # Optionally, you can verify specific menu options or further interactions
    menu_items = profile_settings_menu.find_elements(By.CLASS_NAME, "mat-mdc-menu-item")
    assert len(menu_items) > 0, "No items found in the Answer Settings menu"

    menu_items[0].click()

    profile_container=driver.find_element(By.CLASS_NAME,"profile-container")
    assert profile_container.is_displayed(),"profile section is not visible"

    edit_btn=driver.find_element(By.CLASS_NAME,"edit-btn")
    edit_btn.click()

    user_details_content=driver.find_element(By.CLASS_NAME,"details-content")
    assert user_details_content.is_displayed(),"user details content is not visible"

    details_content = user_details_content.find_elements(By.TAG_NAME, "ion-col")
    assert len(details_content) > 0,"No details found in the user details"

    first_name = driver.find_element(By.XPATH, "//input[@formcontrolname='firstName']")

    # Wait for the element to be rendered
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@formcontrolname="firstName"]')))

    # Check if the input is readonly
    readonly_attribute = first_name.get_attribute('readonly')
    assert readonly_attribute is not True, "Input should be readonly when profileEdit is false."

    # Try interacting with the input field
    try:
        first_name.clear()
        first_name.send_keys("kavitha")
        assert False, "Input field should not be editable when readonly is true."
    except Exception:
        pass

    # last_name = driver.find_element(By.CSS_SELECTOR, 'ion-input[formControlName="lastName"]')
    #
    # # Wait for the element to be rendered
    # WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, 'ion-input[formControlName="lastName"]')))
    #
    # # Check if the input is readonly
    # readonly_attribute = last_name.get_attribute('readonly')
    # assert readonly_attribute is not True, "Input should be readonly when profileEdit is false."
    #
    # # Try interacting with the input field
    # try:
    #     last_name.clear()
    #     last_name.send_keys("ram")
    #     assert False, "Input field should not be editable when readonly is true."
    # except Exception:
    #     pass
    #
    # save_button = driver.find_element(By.XPATH, "//app-submit[@buttonText='Sav']")
    # save_button.click()
    #
