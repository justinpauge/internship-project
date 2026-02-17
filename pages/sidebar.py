from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Sidebar(BasePage):
    # Left menu item by visible text
    OFFPLAN_MENU = (By.XPATH, '//*[self::a or self::button or self::div][normalize-space()="Off-plan"]')

    def go_to_offplan(self):
        self.click(self.OFFPLAN_MENU)
