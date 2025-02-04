from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObject.base import BasePage
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage(BasePage):
    # Locators for elements on the Dashboard page
    CONVERSATION_HISTORY_PANEL = (By.CLASS_NAME, "md.hydrated")  # Locator for history panel
    NEW_CONVERSATION_BUTTON = (By.CLASS_NAME,
                               "new-conversation.md.button.button-solid.ion-activatable.ion-focusable.hydrated")  # Locator for '+ New Conversation' button
    CONVERSATION_LIST = (By.CLASS_NAME, "old-conversation")  # Adjust locator for conversation list
    COMPANY_LOGO = (By.CLASS_NAME, "md hydrated")
    SEE_MORE_BUTTON = (By.CLASS_NAME, "less-more item md item-lines-none hydrated item-label")
    SHADOW_HOST = (By.CSS_SELECTOR, "shadow-host-selector")
    MENU_BUTTON = (By.CLASS_NAME, "div.mat-mdc-menu-trigger.option-btn")

    def verify_conversation_history_panel_display(self):
        """Verify the display of the conversation history panel."""
        panel = self.find_element(*self.CONVERSATION_HISTORY_PANEL)
        return panel.is_displayed()

    def is_new_conversation_button_clickable(self):
        """Check if the '+ New Conversation' button is clickable."""
        button = self.find_element(*self.NEW_CONVERSATION_BUTTON)
        return button.is_enabled()  # Verifies if the button is enabled and clickable

    def click_new_conversation_button(self):
        """Click on the '+ New Conversation' button."""
        self.click(*self.NEW_CONVERSATION_BUTTON)

    def is_company_logo_displayed(self):
        """Check if the company logo is displayed on the page."""
        try:
            logo = self.find_element(*self.COMPANY_LOGO)
            return logo.is_displayed()
        except:
            return False

    def click_menu_icon(self):
        """Click on the menu icon inside the history page."""
        # Wait for the shadow host to be present
        shadow_host = self.find_element(*self.SHADOW_HOST)

        # Access shadow root
        shadow_root = self.driver.execute_script("return arguments[0].shadowRoot", shadow_host)

        # Find menu button inside shadow DOM
        menu_button = shadow_root.find_element(*self.MENU_BUTTON)

        # Click the menu button
        menu_button.click()