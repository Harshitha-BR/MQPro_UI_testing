from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def find_element(self, by, value,):
        return self.wait.until(EC.visibility_of_element_located((by, value)))

    def click(self, by, value):
        element = self.find_element(by, value)
        element.click()

    def send_keys(self, by, value, keys):
        element = self.find_element(by, value)
        element.clear()
        element.send_keys(keys)


    def click_element(self, locator):
        """Click an element."""
        element = self.find_element(locator)
        element.click()

    def get_shadow_root(self, host_element):
        """Get the shadow root of an element."""
        return self.driver.execute_script("return arguments[0].shadowRoot", host_element)
