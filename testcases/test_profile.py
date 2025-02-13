import time
import unittest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObject.login_page import LoginPage
from pageObject.profile import ProfilePage
from utilities.readproperties import ReadConfig


class TestDashboard(unittest.TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.profile_page = None

    def setUp(self):
        # Load configuration values from config.ini
        self.base_url = ReadConfig.geturl()
        self.passcode = ReadConfig.get_password()
        # Initialize WebDriver
        self.driver = webdriver.Chrome()  # Adjust path to the WebDriver if needed
        self.driver.maximize_window()
        self.profile_page = ProfilePage(self.driver)
        login_page = LoginPage(self.driver)
        login_page.login(self.passcode)

        # Login to the app
        time.sleep(10)

    def test_profile_logo_visibility(self):
        self.profile_page.click_profile_logo()  # Ensure the profile menu is clicked first
        assert self.profile_page.is_profile_logo_visible(), "Profile logo is not visible"

    def test_profile_edit_button(self):
        self.profile_page.click_profile_logo()
        self.profile_page.click_edit_button()
        assert self.profile_page.is_first_name_input_editable(), "First Name input is not editable"

    def test_profile_save_button(self):
        self.profile_page.click_profile_logo()
        self.profile_page.click_edit_button()
        self.profile_page.click_save_button()
        # Ensure profile save logic works (this would typically include server-side validation)

    def test_profile_cancel_button(self):
        self.profile_page.click_profile_logo()
        self.profile_page.click_edit_button()
        self.profile_page.click_cancel_button()
        assert self.profile_page.is_first_name_input_readonly(), "First Name should be readonly after Cancel"

    def test_empty_input_fields(self):
        self.profile_page.click_profile_logo()
        self.profile_page.click_edit_button()

    def test_answer_mode_dropdown(self):
        self.profile_page.click_profile_logo()
        self.profile_page.click_edit_button()
        self.profile_page.select_answer_mode("Sentence")
        self.profile_page.click_save_button()
        self.profile_page.check_selected_value("Sentence")

    def test_close_button(self):
        self.profile_page.click_profile_logo()
        self.profile_page.close_profile_modal()
        # Ensure profile modal is closed
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.CLASS_NAME, "profile-container"))
            )
            print("Modal has been successfully closed.")
        except TimeoutException:
            assert False, "Profile modal was not closed successfully."

    def tearDown(self):
        # Close the driver after each test
        self.driver.quit()
