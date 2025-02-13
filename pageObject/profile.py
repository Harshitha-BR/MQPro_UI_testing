from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObject.base import BasePage  # Assuming BasePage is a common base for all page objects

class ProfilePage(BasePage):
    # Locators for profile page actions
    profile_click = (By.XPATH, "//*[@id='main-content']/div[1]/div/div[2]/app-user-logo/div")
    profile_menu = (By.CLASS_NAME, "mat-mdc-menu-panel")
    profile_menu_item = (By.CLASS_NAME, "mat-mdc-menu-item")
    profile_container = (By.CLASS_NAME, "profile-container")
    edit_button = (By.CLASS_NAME, "edit-btn")
    save_button = (By.XPATH, "//app-submit[@buttonText='Save']")
    cancel_button = (By.XPATH, "//app-submit[@buttonText='Cancel']")
    first_name_input = (By.CSS_SELECTOR, '[formControlName="firstName"]')
    dropdown = (By.CSS_SELECTOR, "mat-select")
    option_sentence = (By.XPATH, "//mat-option[@value='Sentence']")
    option_graph = (By.XPATH, "//mat-option[@value='Graph']")
    option_table = (By.XPATH, "//mat-option[@value='Table']")
    selected_value_col = (By.CLASS_NAME, "selected-value")
    close_button = (By.CLASS_NAME, "close-btn")

    def click_profile_logo(self):
        profile_logo = self.driver.find_element(*self.profile_click)
        profile_logo.click()

        # Wait for the profile menu to appear
        profile_menu = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.profile_menu)
        )
        assert profile_menu.is_displayed(), "Profile menu is not displayed"

        # Click the first menu item (Profile option)
        profile_menu_items = profile_menu.find_elements(*self.profile_menu_item)
        assert profile_menu_items[0].is_displayed(), "Profile option is not displayed"
        profile_menu_items[0].click()

        # Wait for the profile container to be visible
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.profile_container)
        )

    def click_edit_button(self):
        edit_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.edit_button)
        )
        edit_button.click()

    def click_save_button(self):
        save_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.save_button)
        )
        save_button.click()

    def click_cancel_button(self):
        cancel_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.cancel_button)
        )
        cancel_button.click()

    def select_answer_mode(self, mode="Sentence"):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.dropdown)
        )
        dropdown.click()

        # Select the correct option based on the provided mode
        if mode == "Sentence":
            option = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.option_sentence)
            )
        elif mode == "Graph":
            option = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.option_graph)
            )
        else:  # Default to Table
            option = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.option_table)
            )

        option.click()

    def check_selected_value(self, expected_value):
        selected_value = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.selected_value_col)
        )
        assert selected_value.text == expected_value, f"Expected '{expected_value}', but got {selected_value.text}"

    def close_profile_modal(self):
        close_button = self.driver.find_element(*self.close_button)
        close_button.click()

        # Wait until the profile container becomes invisible or is removed from the DOM
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(self.profile_container)
        )

    # Helper Methods to check input field attributes
    def is_profile_logo_visible(self):
        profile_logo = self.driver.find_element(*self.profile_click)
        return profile_logo.is_displayed()

    def is_first_name_input_editable(self):
        first_name_input = self.driver.find_element(*self.first_name_input)
        return first_name_input.is_enabled()

    def is_first_name_input_readonly(self):
        first_name_input = self.driver.find_element(*self.first_name_input)
        return first_name_input.get_attribute("readonly") is not None
