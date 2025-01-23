
import pytest
from utilities.readproperties import ReadConfig
from utilities.utils import get_org_passcode_data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


LOGIN_URL = ReadConfig.geturl()  # Get the login URL from the login section
PASSCODE = ReadConfig.get_password()
CHAT_URL = "https://sandbox.mqpro.tibilsolutions.com/chat-board"  # Get the login URL from the login section

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

def test_open_question_settings_menu(setup,):
    driver=setup
    # Locate the image element that triggers the mat-menu
    faq_card=driver.find_element(By.TAG_NAME,"ion-card")

    faq_card.click()
    settings_img = driver.find_element(By.CSS_SELECTOR, ".settings-img")

    # Ensure the image is clickable and visibl
    assert settings_img.is_displayed(), "Settings image is not visible"

    # Perform a click action to trigger the mat-menu
    settings_img.click()

    # Verify if the mat-menu is visible after click
    answer_settings_menu = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "mat-mdc-menu-panel"))
    )
    assert answer_settings_menu.is_displayed(), "Answer Settings menu is not visible"

    # Optionally, you can verify specific menu options or further interactions
    menu_items = answer_settings_menu.find_elements(By.CLASS_NAME, "mat-mdc-menu-item")
    assert len(menu_items) > 0, "No items found in the Answer Settings menu"

def test_star_question(setup,):
    driver=setup
    # Locate the image element that triggers the mat-menu
    faq_card=driver.find_element(By.TAG_NAME,"ion-card")

    faq_card.click()
    settings_img = driver.find_element(By.CSS_SELECTOR, ".settings-img")

    # Ensure the image is clickable and visibl
    assert settings_img.is_displayed(), "Settings image is not visible"

    # Perform a click action to trigger the mat-menu
    settings_img.click()

    # Verify if the mat-menu is visible after click
    answer_settings_menu = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "mat-mdc-menu-panel"))
    )
    assert answer_settings_menu.is_displayed(), "Answer Settings menu is not visible"

    # Optionally, you can verify specific menu options or further interactions
    menu_items = answer_settings_menu.find_elements(By.CLASS_NAME, "mat-mdc-menu-item")
    assert len(menu_items) > 0, "No items found in the Answer Settings menu"

    menu_items[0].click()

    star_icon=driver.find_element(By.CLASS_NAME,"star-icon")
    assert star_icon.is_displayed(),"star icon is not visible"

def test_unstar_question(setup,):
    driver=setup
    # Locate the image element that triggers the mat-menu
    faq_card=driver.find_element(By.TAG_NAME,"ion-card")

    faq_card.click()
    settings_img = driver.find_element(By.CSS_SELECTOR, ".settings-img")

    # Ensure the image is clickable and visibl
    assert settings_img.is_displayed(), "Settings image is not visible"

    # Perform a click action to trigger the mat-menu
    settings_img.click()

    # Verify if the mat-menu is visible after click
    answer_settings_menu = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "mat-mdc-menu-panel"))
    )
    assert answer_settings_menu.is_displayed(), "Answer Settings menu is not visible"

    # Optionally, you can verify specific menu options or further interactions
    menu_items = answer_settings_menu.find_elements(By.CLASS_NAME, "mat-mdc-menu-item")
    assert len(menu_items) > 0, "No items found in the Answer Settings menu"

    menu_items[0].click()
def test_suggest_box_open(setup,):
    driver=setup

    suggest_box = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "click-trigger"))
    )
    suggest_box.click()

    suggest_box_option = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "wrapper"))
    )
    assert suggest_box_option.is_displayed(), "Answer Settings menu is not visible"

    starred_tab=driver.find_element(By.CLASS_NAME,"inactive-tab")
    starred_tab.click()

    faq_list = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "faq-list"))
    )
    assert faq_list.is_displayed(), "Answer Settings menu is not visible"

    starred_items = faq_list.find_elements(By.CLASS_NAME, "suggested-item")

    assert len(starred_items) > 0,"No starred questions found"
    delete_option = driver.find_element(By.CLASS_NAME, "setting-icon")
    delete_option.click()

    answer_settings_menu = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "mat-mdc-menu-panel"))
    )
    assert answer_settings_menu.is_displayed(), "Answer Settings menu is not visible"

    # Optionally, you can verify specific menu options or further interactions
    menu_items = answer_settings_menu.find_elements(By.CLASS_NAME, "mat-mdc-menu-item")
    assert len(menu_items) > 0, "No items found in the Answer Settings menu"

    menu_items[0].click()








