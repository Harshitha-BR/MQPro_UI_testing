import time
import unittest
import configparser
from selenium import webdriver
from pageObject.login_page import LoginPage
from pageObject.History import DashboardPage
from selenium.webdriver.support import expected_conditions as EC

from pageObject.profile import ProfilePage


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

    def test_click_profile(self):
        home_page = ProfilePage(self.driver)
        home_page.profile_click()



