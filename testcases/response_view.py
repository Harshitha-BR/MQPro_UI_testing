import time
import pytest
from utilities.readproperties import ReadConfig
from utilities.utils import get_org_passcode_data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObject.chat_board import ChatPage  # Import ChatPage object

LOGIN_URL = ReadConfig.geturl()  # Get the login URL from the login section
PASSCODE = ReadConfig.get_password()


@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(LOGIN_URL)

    passcode_fields = driver.find_elements(By.XPATH, "//input[@maxlength='1']")
    for i, field in enumerate(passcode_fields):
        field.clear()
        field.send_keys(PASSCODE[i])

    login_button = driver.find_element(By.XPATH, "//app-submit[@buttonText='LOGIN']")
    login_button.click()

    yield driver
    driver.quit()


def test_open_answer_settings_menu(setup):
    driver = setup
    chat_page = ChatPage(driver)  # Initialize ChatPage

    # Open FAQ card and settings menu
    chat_page.click_faq_card()
    chat_page.open_response_settings_menu()

    # Verify if the settings menu is visible
    assert chat_page.is_settings_menu_displayed(), "Answer Settings menu is not visible"



def test_table_view(setup):
    driver = setup
    chat_page = ChatPage(driver)  # Initialize ChatPage

    # Open FAQ card and settings menu
    chat_page.click_faq_card()
    chat_page.open_response_settings_menu()

    # Click the second menu item (assuming it corresponds to table view)
    chat_page.click_menu_item(1)

    # Verify if the table container is visible
    assert chat_page.is_table_container_displayed(), "Table view is not visible"


def test_graph_view(setup):
    driver = setup
    chat_page = ChatPage(driver)  # Initialize ChatPage

    # Open FAQ card and settings menu
    chat_page.click_faq_card()
    chat_page.open_response_settings_menu()

    # Click the third menu item (assuming it corresponds to graph view)
    chat_page.click_menu_item(2)

    # Verify if the graph container is visible
    assert chat_page.is_graph_container_displayed(), "Graph view is not visible"


def test_download_option(setup):
    driver = setup
    chat_page = ChatPage(driver)  # Initialize ChatPage

    # Open FAQ card and settings menu
    chat_page.click_faq_card()
    chat_page.open_response_settings_menu()

    # Click the fifth menu item (assuming it corresponds to download option)
    chat_page.click_menu_item(4)

    # Perform additional assertions or checks here if necessary
    assert chat_page.is_table_container_displayed(), "Table container is not displayed after download"
