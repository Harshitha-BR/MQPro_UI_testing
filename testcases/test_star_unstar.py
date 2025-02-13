import time
import unittest
import configparser
from selenium import webdriver
from pageObject.login_page import LoginPage
from pageObject.newchat import NewchatPage
from pageObject.profile import ProfilePage
from utilities.readproperties import ReadConfig


class TestDashboard(unittest.TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.hom_page = None

    def setUp(self):
        # Load configuration values from config.ini
        self.base_url = ReadConfig.geturl()
        self.passcode = ReadConfig.get_password()

        # Initialize WebDriver
        self.driver = webdriver.Chrome()  # Adjust path to the WebDriver if needed
        self.driver.maximize_window()
        login_page = LoginPage(self.driver)
        login_page.login(self.passcode)

        # Login to the app
        # login_page = LoginPage(self.driver)
        # login_page.login(self.passcode)
        time.sleep(10)

    def test_open_question_settings_menu(self):
        home_page = NewchatPage(self.driver);
        home_page.click_faq_card()  # Initialize ChatPage instance
        home_page.open_question_settings_menu()

    def test_star_question(self):
        home_page = NewchatPage(self.driver);\

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

    def test_suggest_box_open(self):
        home_page = NewchatPage(self.driver)


        home_page.open_suggest_box()

        assert home_page.is_suggest_box_open(), "Suggest box is not open"

        home_page.click_stared_tab()

        starred_items = home_page.get_suggested_items()
        assert len(starred_items) > 0, "No starred questions found"

        # Click the settings icon on the starred item
        home_page.click_setting_icon()



