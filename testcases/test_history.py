import time
import unittest
import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObject.login_page import LoginPage
from pageObject.History import DashboardPage
from selenium.webdriver.support import expected_conditions as EC

from pageObject.newchat import NewchatPage
from utilities.readproperties import ReadConfig


class TestDashboard(unittest.TestCase):
    def setUp(self):
        # Load configuration values from config.ini
        self.base_url = ReadConfig.geturl()
        self.passcode = ReadConfig.get_password()

        # Initialize WebDriver
        self.driver = webdriver.Chrome()  # Adjust path to the WebDriver if needed
        self.driver.maximize_window()
        login_page = LoginPage(self.driver)
        login_page.login(self.passcode)
        self.history_page = DashboardPage(self.driver)

        time.sleep(10)

    def test_conversation_history_panel_display(self):
        """Test to verify the display of the conversation history panel."""
        is_displayed = self.history_page.verify_conversation_history_panel_display()
        self.assertTrue(is_displayed, "Conversation history panel is not displayed.")

    def test_new_conversation_button_displayed(self):
        """Verify the '+ New Conversation' button is displayed."""
        button = self.history_page.get_new_conversation_button()
        self.assertTrue(button.is_displayed, "+ New Conversation button is not visible")

    def test_new_conversation_button_clickable(self):
        """Verify the '+ New Conversation' button is clickable."""
        button = self.history_page.get_new_conversation_button()
        self.assertTrue(button.is_enabled(), "+ New Conversation button is not clickable")

    def test_company_logo_displayed(self):
        """Verify the company logo is displayed."""
        company_logo = self.history_page.get_company_logo()
        self.assertTrue(company_logo.is_displayed, "Company logo is not visible")

    def test_see_more_button(self):
        """Verify that the 'See More' button is displayed."""
        button = self.history_page.get_see_more_button()
        self.assertTrue(button.is_displayed, "'See More' button is not visible")

    def test_see_less_button(self):
        """Verify that the 'See Less' button is displayed."""
        button = self.history_page.get_see_less_button()
        self.assertTrue(button.is_displayed, "'See Less' button is not visible")

    def test_history_option_button(self):
        """Verify that the history option button is displayed."""
        button = self.history_page.get_history_option_button()
        self.assertTrue(button.is_displayed, "History option button is not visible")

    def test_old_conversations_section(self):
        """Verify the old conversations section is visible."""
        old_conversations = self.history_page.get_old_conversations_section()
        self.assertTrue(old_conversations.is_displayed, "Old conversations section is not visible")

    def test_conversations_items_displayed(self):
        """Verify that the conversation items are displayed."""
        conversations_items = self.history_page.get_conversations_items()
        self.assertGreater(len(conversations_items), 0, "No conversation items found")

    def test_conversation_topic_displayed(self):
        """Verify the conversation topic is displayed."""
        conversations_items = self.history_page.get_conversations_items()
        for conversation_item in conversations_items:
            conversation_topic = self.history_page.get_conversation_topic(conversation_item)
            self.assertTrue(conversation_topic.is_displayed, "Conversation topic is not visible")

    def test_conversation_option_button_displayed(self):
        """Verify the conversation option button is displayed."""
        conversations_items = self.history_page.get_conversations_items()
        for conversation_item in conversations_items:
            conversation_option_btn = self.history_page.get_conversation_option_button(conversation_item)
            self.assertTrue(conversation_option_btn.is_displayed, "Conversation option button is not visible")


    # def tearDown(self):
    #     # Quit the WebDriver
    #     self.driver.quit()
#
#
if __name__ == "__main__":
    unittest.main()