import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObject.login_page import LoginPage


from pageObject.newchat import NewchatPage
from utilities.readproperties import ReadConfig


class TestDashboard(unittest.TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.hom_page = None

    def setUp(self):
        # Load configuration values from config.ini
        self.base_url = ReadConfig.geturl()
        self.passcode = ReadConfig.get_password()
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

    def test_open_answer_settings_menu(self):
        home_page = NewchatPage(self.driver)
        home_page.click_faq_card()
        home_page.open_response_settings_menu() # Initialize ChatPage
        assert home_page.is_settings_menu_displayed(), "Answer Settings menu is not visible"

    def test_table_view(self):
        home_page = NewchatPage(self.driver)
        # Open FAQ card and settings menu
        home_page.click_faq_card()
        home_page.open_response_settings_menu()

        # Click the second menu item (assuming it corresponds to table view)
        home_page.click_menu_item(1)

        # Verify if the table container is visible
        assert home_page.is_table_container_displayed(), "Table view is not visible"

    def test_graph_view(self):
        home_page = NewchatPage(self.driver) # Initialize ChatPage

        # Open FAQ card and settings menu
        home_page.click_faq_card()
        home_page.open_response_settings_menu()

        # Click the third menu item (assuming it corresponds to graph view)
        home_page.click_menu_item(2)

        # Verify if the graph container is visible
        assert home_page.is_graph_container_displayed(), "Graph view is not visible"

    def test_copy_option(self):
        home_page = NewchatPage(self.driver)  # Initialize ChatPage

        # Open FAQ card and settings menu
        home_page.click_faq_card()
        home_page.open_response_settings_menu()

        # Click the fifth menu item (assuming it corresponds to download option)
        home_page.click_menu_item(3)

    def test_download_option(self):
        home_page = NewchatPage(self.driver) # Initialize ChatPage

        # Open FAQ card and settings menu
        home_page.click_faq_card()
        home_page.open_response_settings_menu()

        # Click the fifth menu item (assuming it corresponds to download option)
        home_page.click_menu_item(4)

        # Perform additional assertions or checks here if necessary
        # assert home_page.is_table_container_displayed(), "Table container is not displayed after download"

