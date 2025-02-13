from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObject.base import BasePage
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage(BasePage):
    # Locators for elements on the Dashboard page
    conversation_history_panel_locator = (By.ID, "main-content")
    new_conversation_button_locator = (By.CLASS_NAME, "new-conversation")
    company_logo_locator = (By.CLASS_NAME, "org-logo")
    see_more_button_locator = (By.CLASS_NAME, "see-more-btn")
    see_less_button_locator = (By.CLASS_NAME, "see-less-btn")
    history_option_button_locator = (By.CLASS_NAME, "option-btn")
    old_conversation_section_locator = (By.CLASS_NAME, "old-conversation")
    conversation_item_locator = (By.CLASS_NAME, "conversation-item")
    conversation_title_locator = (By.CLASS_NAME, "conversation-title")
    conversation_option_button_locator = (By.CLASS_NAME, "option-btn")

    def verify_conversation_history_panel_display(self):
        """Verify if the conversation history panel is displayed."""
        try:
            panel = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.conversation_history_panel_locator)
            )
            return panel.is_displayed
        except:
            return False

    def get_new_conversation_button(self):
        """Get the '+ New Conversation' button."""
        return self.driver.find_element(*self.new_conversation_button_locator)

    def get_company_logo(self):
        """Get the company logo."""
        return self.driver.find_element(*self.company_logo_locator)

    def get_see_more_button(self):
        """Get the 'See More' button."""
        return self.driver.find_element(*self.see_more_button_locator)

    def get_see_less_button(self):
        """Get the 'See Less' button."""
        return self.driver.find_element(*self.see_less_button_locator)

    def get_history_option_button(self):
        """Get the history option button."""
        return self.driver.find_element(*self.history_option_button_locator)

    def get_old_conversations_section(self):
        """Get the old conversations section."""
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.old_conversation_section_locator)
        )

    def get_conversations_items(self):
        """Get all conversation items."""
        old_conversations = self.get_old_conversations_section()
        return old_conversations.find_elements(*self.conversation_item_locator)

    def get_conversation_topic(self, conversation_item):
        """Get the conversation topic from a conversation item."""
        return conversation_item.find_element(*self.conversation_title_locator)

    def get_conversation_option_button(self, conversation_item):
        """Get the conversation option button from a conversation item."""
        return conversation_item.find_element(*self.conversation_option_button_locator)