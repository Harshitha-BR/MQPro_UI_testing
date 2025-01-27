from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.passcode_fields = driver.find_elements(By.XPATH, "//input[@maxlength='1']")
        self.logo = driver.find_element(By.XPATH, "//img[@alt='Mq Title Logo']")
        self.welcome_text = driver.find_element(By.XPATH, "//h2[contains(text(), 'Welcome to')]")
        self.passcode_field = driver.find_element(By.CLASS_NAME, "otp-inputGroup")
        self.login_button = driver.find_element(By.XPATH, "//app-submit[@buttonText='LOGIN']")
        self.error_message_locator = (By.CLASS_NAME, "error-message")
        self.faq_card=driver.find_element(By.TAG_NAME,"ion-card")

    def enter_passcode(self, passcode):
        """Method to enter passcode into the OTP fields"""
        for i, field in enumerate(self.passcode_fields):
            field.clear()  # Clear the field before entering
            field.send_keys(passcode[i])

    def verify_passcode_fields(self, passcode):
        """Method to verify that passcode fields have been populated correctly"""
        for i, field in enumerate(self.passcode_fields):
            assert field.get_attribute('value') == passcode[
                i], f"Passcode field {i + 1} does not match the expected value"

    def check_logo_displayed(self):
        """Check if the logo is displayed on the page"""
        return self.logo.is_displayed()

    def check_welcome_text_displayed(self):
        """Check if the welcome text is displayed on the page"""
        return self.welcome_text.is_displayed()

    def check_passcode_field_displayed(self):
        """Check if the passcode input fields are visible"""
        return self.passcode_field.is_displayed()

    def check_login_button_displayed(self):
        """Check if the login button is visible"""
        return self.login_button.is_displayed()

    def click_login_button(self):
        """Click the login button"""
        self.login_button.click()

    def is_login_button_disabled(self):
        """Check if the login button is enabled"""
        return self.login_button.get_attribute("disabled") is  True

    def wait_for_error_message(self, timeout=10):
        """Helper method to wait for and return the error message element"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.error_message_locator)
            )
        except Exception as e:
            raise AssertionError("Error message not found: " + str(e))

    def click_faq_card(self):
        """Method to click on the FAQ card"""
        self.faq_card.click()
