from selenium.webdriver.common.by import By
from pageObject.base import BasePage


class LoginPage(BasePage):
    URL = "https://sandbox.mqpro.tibilsolutions.com"

    PASSWORD_INPUT = (By.XPATH, "//input[@maxlength='1']")  # Update if locator differs
    LOGIN_BUTTON = (By.XPATH, "//app-submit[@buttonText='LOGIN']")  # Update if locator differs

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(self.URL)

    def enter_password(self, password):
        self.send_keys(*self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(*self.LOGIN_BUTTON)

    def login(self, password):
        self.enter_password(password)
        self.click_login()
