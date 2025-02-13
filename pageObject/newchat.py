from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObject.base import BasePage
from selenium.webdriver.support import expected_conditions as EC

class NewchatPage(BasePage):

    GREETING_TEXTBOX = (By.CLASS_NAME, "native-wrapper sc-ion-input-md sc-ion-input-md-s")


    greeting_textbox = (By.CSS_SELECTOR, "input.native-input.sc-ion-input-md")
    submit_button = (By.XPATH, "//*[@id='main-content']/div[3]/form/app-submit/ion-button")
    # menu_panel = (By.CLASS_NAME, "mat-mdc-menu-panel")
    # menu_item = (By.CLASS_NAME, "mat-mdc-menu-item")
    # star_button = (By.CSS_SELECTOR, "star-icon")
    # unstar_button = (By.CSS_SELECTOR, "star-icon")

    faq_card = (By.TAG_NAME, "ion-card")
    question_settings_img = (By.CSS_SELECTOR, ".settings-img")  # Question Settings
    response_settings_img = (By.CSS_SELECTOR, ".response-avatar .settings-img")  # Response Settings
    menu_panel = (By.CLASS_NAME, "mat-mdc-menu-panel")
    menu_item = (By.CLASS_NAME, "mat-mdc-menu-item")
    star_icon = (By.CLASS_NAME, "star-icon")
    suggest_box_trigger = (By.CLASS_NAME, "suggest-box")
    suggest_box_wrapper = (By.CLASS_NAME, "wrapper")
    faq_list = (By.CLASS_NAME, "faq-list")
    stared_items = (By.CLASS_NAME, "suggested-item")
    inactive_tab = (By.CLASS_NAME, "inactive-tab")
    setting_icon = (By.CLASS_NAME, "setting-icon")
    table_container = (By.CLASS_NAME, "carbon-footprint-card")
    graph_container = (By.CLASS_NAME, "graph-container")

    def get_greeting_text(self):
        return self.driver.find_element(*self.greeting_textbox).get_attribute("placeholder")

    def click_submit_button(self):
        self.driver.find_element(*self.submit_button).click()

    def enter_text(self, text):
        self.driver.find_element(*self.greeting_textbox).send_keys(text)

    def is_three_dot_menu_visible(self):
        return self.driver.find_element(*self.menu_panel).is_displayed()
    #
    # def click_three_dot_menu(self):
    #     self.driver.find_element(*self.menu_item).click()
    #
    # def click_star_button(self):
    #     self.driver.find_element(*self.star_button).click()
    #
    # def click_unstar_button(self):
    #     self.driver.find_element(*self.unstar_button).click()
    def click_faq_card(self):
        """Click the FAQ card to open the settings menu."""
        faq_card_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.faq_card)
        )
        faq_card_element.click()

        # Function to click the Question Settings image

    def click_question_settings_img(self):
        """Click the Question Settings image to open the settings menu."""
        question_settings_img_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.question_settings_img)
        )
        question_settings_img_element.click()

        # Function to click the Response Settings image

    def click_response_settings_img(self):
        """Click the Response Settings image to open the settings menu."""
        response_settings_img_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.response_settings_img)
        )
        response_settings_img_element.click()

        # Open Question Settings Menu

    def open_question_settings_menu(self):
        """Open the Question Settings menu by clicking the question settings image."""
        self.click_question_settings_img()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.menu_panel)
        )

        # Open Response Settings Menu

    def open_response_settings_menu(self):
        """Open the Response Settings menu by clicking the response settings image."""
        self.click_response_settings_img()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.menu_panel)
        )

        # Function to click a menu item by index

    def click_menu_item(self, index):
        """Click a menu item by index."""
        menu_panel = self.driver.find_element(*self.menu_panel)
        menu_items = menu_panel.find_elements(*self.menu_item)

        if 0 <= index < len(menu_items):
            menu_items[index].click()
        else:
            raise IndexError(f"Menu item index {index} is out of range. Available options: 0-{len(menu_items) - 1}.")

        # Function to check if the star icon is displayed

    def is_star_icon_displayed(self):
        """Check if the star icon is displayed"""
        star_icon_element = self.driver.find_element(*self.star_icon)
        return star_icon_element.is_displayed

        # Function to open the suggestion box

    def open_suggest_box(self):
        """Open the suggest box"""
        suggest_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.suggest_box_trigger)
        )
        # suggest_box=self.driver.find_element(self.suggest_box_trigger)
        suggest_box.click()

        # Function to get the list of starred items

    def get_suggested_items(self):
        """Get the list of starred items"""
        faq_list = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.faq_list)
        )
        starred_items = faq_list.find_elements(*self.stared_items)
        return starred_items

        # Function to check if the suggestion box is open

    def is_suggest_box_open(self):
        """Check if the suggest box is open"""
        suggest_box_option = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.suggest_box_wrapper)
        )
        return suggest_box_option.is_displayed()

        # Function to click the starred tab

    def click_stared_tab(self):
        """Click the starred tab"""
        starred_tab = self.driver.find_element(*self.inactive_tab)
        starred_tab.click()

        # Function to click the settings icon

    def click_setting_icon(self):
        """Click the setting icon"""
        setting_icon = self.driver.find_element(*self.setting_icon)
        setting_icon.click()

        # Function to check if the table container is displayed

    def is_table_container_displayed(self):
        """Check if the table container is displayed."""
        table_container_element = self.driver.find_element(*self.table_container)
        return table_container_element.is_displayed()

        # Function to check if the graph container is displayed

    def is_graph_container_displayed(self):
        """Check if the graph container is displayed."""
        graph_container_element = self.driver.find_element(*self.graph_container)
        return graph_container_element.is_displayed()

        # Function to check if the settings menu is displayed

    def is_settings_menu_displayed(self):
        """Check if the Answer Settings menu is displayed."""
        try:
            menu_panel_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.menu_panel)
            )
            return menu_panel_element.is_displayed()
        except:
            return False  # Return False if the element is not found or not visible

    def enter_greeting(self, text):
        self.driver.find_element(*self.greeting_textbox).send_keys(text)

    def submit_greeting(self):
        self.driver.find_element(*self.submit_button).click()

    def is_menu_panel_visible(self):
        return self.driver.find_element(*self.menu_panel).is_displayed()

    def click_settings_icon(self):
        self.driver.find_element(*self.setting_icon).click()

    def is_menu_item_clickable(self):
        return self.driver.find_element(*self.menu_item).is_enabled()

    def open_menu_panel(self):
        self.driver.find_element(*self.setting_icon).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.menu_panel))