import unittest
import configparser
from selenium import webdriver
from pageObject.login_page import LoginPage


class TestLogin(unittest.TestCase):
    def setUp(self):
        # Load configuration values from config.ini
        config = configparser.ConfigParser()
        config.read("/home/harshitha/Documents/MQPro_UI_testing/configuration/config.ini")
        self.passcode = config["LOGIN"]["passcode"]
        self.base_url = config["URL"]["base_url"]

        # Initialize WebDriver
        self.driver = webdriver.Chrome()  # Adjust path to the WebDriver if needed
        self.driver.maximize_window()

    def test_valid_login(self):
        # Perform login
        login_page = LoginPage(self.driver)
        login_page.login(self.passcode)

        # Add verification for successful login (adjust based on your app)
        self.assertIn("MQ PRO", self.driver.title)  # Example assertion

    # def tearDown(self):
    #     # Quit the WebDriver
    #     self.driver.quit()


if __name__ == "__main__":
    unittest.main()
