import time
import unittest
import configparser
from selenium import webdriver
from pageObject.login_page import LoginPage
from pageObject.History import DashboardPage
from selenium.webdriver.support import expected_conditions as EC

from pageObject.newchat import NewchatPage


class TestDashboard(unittest.TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.hom_page = None

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

    def test_greeting_text(self):
        home_page = NewchatPage(self.driver)
        greeting_text = home_page.get_greeting_text()
        self.assertEqual(greeting_text, "Hi Joseph, please select an FAQ or feel free to ask a question")

    def test_submit_button_no_input(self):
        home_page = NewchatPage(self.driver)
        home_page.click_submit_button()
        # Add assertion to check for any error message or behavior when no input is provided

    def test_non_sales_related_input(self):
        home_page = NewchatPage(self.driver)
        home_page.enter_text("What is the weather today?")
        home_page.click_submit_button()
        # Add assertion to check how the system handles non-sales-related input

    def test_sales_related_input(self):
        home_page = NewchatPage(self.driver)
        home_page.enter_text("What are the top 5 products by sales?")
        home_page.click_submit_button()

    def test_star_question(self):
        home_page = NewchatPage(self.driver)
        home_page.click_faq_card()
        home_page.open_question_settings_menu()

        # Star the question
        home_page.click_menu_item(0)

        # Check if the star icon is displayed
        assert home_page.is_star_icon_displayed(), "Star icon is not visible"

    def test_unstar_question(self):
        home_page = NewchatPage(self.driver)
        home_page.click_faq_card()
        home_page.open_question_settings_menu()

        # Unstar the question
        home_page.click_menu_item(0)

    def test_invalid_prompt_menu_not_appear(self):
        home_page = NewchatPage(self.driver)
        home_page.enter_text("What is the weather today?")
        home_page.click_submit_button()
        # assert home_page.is_three_dot_menu_visible(), "3-dot Menu should not appear for invalid prompt"

    def test_valid_prompt_menu_appears(self):
        home_page = NewchatPage(self.driver)
        home_page.enter_text("What are the top 5 products by sales?")
        home_page.click_submit_button()
        assert home_page.is_star_icon_displayed(), "3-dot Menu should appear for valid response"


    def test_menu_clickable(self):
        home_page = NewchatPage(self.driver)
        home_page.click_faq_card()
        home_page.open_question_settings_menu()

        # Star the question
        home_page.click_menu_item(0)

        # Check if the star icon is displayed
        assert home_page.is_star_icon_displayed(), "Star icon is not visible"

    def test_popover_menu_opens(self):
        home_page = NewchatPage(self.driver)
        home_page.click_faq_card()
        home_page.open_question_settings_menu()

        # Star the question
        home_page.click_menu_item(0)
        assert home_page.is_star_icon_displayed(),"Popover menu should open on clicking the three dots"
