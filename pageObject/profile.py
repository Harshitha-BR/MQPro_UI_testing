from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObject.base import BasePage
from selenium.webdriver.support import expected_conditions as EC

class ProfilePage(BasePage):

    profile_click = (By.XPATH, "//*[@id='main-content']/div[1]/div/div[2]/app-user-logo/div")

    def profile_click(self):
        element = self.driver.find_element(*self.profile_click)  # Locate the profile element
        element.click()  # Click the profile button