import time
import unittest
import configparser
from selenium import webdriver
from pageObject.login_page import LoginPage
from pageObject.History import DashboardPage
from selenium.webdriver.support import expected_conditions as EC


class TestDashboard(unittest.TestCase):
    def setUp(self):
        # Load configuration values from config.ini
        config = configparser.ConfigParser()
        config.read("C:/Users/Adithya G/formyself/MQPro_UI_testing/configuration/config.ini")
        self.base_url = config["URL"]["base_url"]
        self.passcode = config["LOGIN"]["passcode"]
        # self.base_url = config["URL"]["base_url"]


        # Initialize WebDriver
        self.driver = webdriver.Chrome()  # Adjust path to the WebDriver if needed
        self.driver.maximize_window()
        login_page = LoginPage(self.driver)
        login_page.login(self.passcode)

        # Login to the app
        # login_page = LoginPage(self.driver)
        # login_page.login(self.passcode)
        time.sleep(10)

    def test_conversation_history_panel_display(self):
        """Test to verify the display of the conversation history panel."""
        history_page = DashboardPage(self.driver)
        is_displayed = history_page.verify_conversation_history_panel_display()
        self.assertTrue(is_displayed, "Conversation history panel is not displayed.")

    def test_new_conversation_button_clickable(self):
        """Verify the '+ New Conversation' button is clickable."""
        history_page = DashboardPage(self.driver)
        self.assertTrue(history_page.is_new_conversation_button_clickable(),
                        "New Conversation button is not clickable.")

    def test_company_logo_displayed(self):
        # Navigate to the History Page and check the logo
        history_page = DashboardPage(self.driver)
        is_logo_displayed = history_page.is_company_logo_displayed()

        # Assertion
        # self.assertTrue(is_logo_displayed, 'Company logo is not displayed on the History Page')

    def test_click_menu_icon(self):
        """Verify that clicking the menu icon works correctly."""
        history_page = DashboardPage(self.driver)
        clicked = history_page.click_menu_icon()

        # Assert that menu icon was clicked successfully
        self.assertTrue(clicked, "Failed to click menu icon")



    def tearDown(self):
        # Quit the WebDriver
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()