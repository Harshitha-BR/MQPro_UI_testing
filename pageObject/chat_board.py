from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ChatBoardPage:
    def __init__(self, driver):
        self.driver = driver

    def click_faq_card(self):
        """Click on the FAQ card to open the menu."""
        faq_card = self.driver.find_element(By.TAG_NAME, "ion-card")
        faq_card.click()

    def get_settings_image(self):
        """Return the settings image element."""
        return self.driver.find_element(By.CSS_SELECTOR, ".response-avatar .settings-img")

    def open_answer_settings_menu(self):
        """Click the settings image to open the answer settings menu."""
        settings_img = self.get_settings_image()
        settings_img.click()

        # Wait until the menu is visible
        answer_settings_menu = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "mat-mdc-menu-panel"))
        )
        return answer_settings_menu

    def get_menu_items(self):
        """Return all the items in the answer settings menu."""
        answer_settings_menu = self.open_answer_settings_menu()
        menu_items = answer_settings_menu.find_elements(By.CLASS_NAME, "mat-mdc-menu-item")
        return menu_items

    def click_menu_item(self, index):
        """Click on a specific menu item based on its index."""
        menu_items = self.get_menu_items()
        menu_items[index].click()

    def is_table_view_displayed(self):
        """Check if the table view is displayed."""
        table_container = self.driver.find_element(By.CLASS_NAME, "carbon-footprint-card")
        return table_container.is_displayed()

    def is_graph_view_displayed(self):
        """Check if the graph view is displayed."""
        graph_container = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "graph-container"))
        )
        return graph_container.is_displayed()
