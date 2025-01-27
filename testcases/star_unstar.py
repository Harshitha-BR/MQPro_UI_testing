import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities.readproperties import ReadConfig
from pageObject.chat_board import ChatPage  # Import the ChatPage class


LOGIN_URL = ReadConfig.geturl()  # Get the login URL from the login section
PASSCODE = ReadConfig.get_password()


@pytest.fixture(scope="function")
def setup():
    # Initialize WebDriver (using Chrome in this example)
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  # Implicit wait to handle loading time
    driver.get(LOGIN_URL)

    # Enter Passcode to log in
    passcode_fields = driver.find_elements(By.XPATH, "//input[@maxlength='1']")
    for i, field in enumerate(passcode_fields):
        field.clear()
        field.send_keys(PASSCODE[i])
    login_button = driver.find_element(By.XPATH, "//app-submit[@buttonText='LOGIN']")
    login_button.click()

    yield driver
    driver.quit()


def test_open_question_settings_menu(setup):
    driver = setup
    chat_page = ChatPage(driver)
    chat_page.click_faq_card()# Initialize ChatPage instance
    chat_page.open_question_settings_menu()


def test_star_question(setup):
    driver = setup
    chat_page = ChatPage(driver)
    chat_page.click_faq_card()
    chat_page.open_question_settings_menu()

    # Star the question
    chat_page.click_menu_item(0)

    # Check if the star icon is displayed
    assert chat_page.is_star_icon_displayed(), "Star icon is not visible"


def test_unstar_question(setup):
    driver = setup
    chat_page = ChatPage(driver)
    chat_page.click_faq_card()
    chat_page.open_question_settings_menu()

    # Unstar the question
    chat_page.click_menu_item(0)


def test_suggest_box_open(setup):
    driver = setup
    chat_page = ChatPage(driver)

    chat_page.open_suggest_box()

    assert chat_page.is_suggest_box_open(), "Suggest box is not open"

    chat_page.click_stared_tab()

    starred_items = chat_page.get_suggested_items()
    assert len(starred_items) > 0, "No starred questions found"

    # Click the settings icon on the starred item
    chat_page.click_setting_icon()
