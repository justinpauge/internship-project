from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class Sidebar(BasePage):

    OFF_PLAN_BUTTON = (By.XPATH, "//button[contains(., 'Off')]")

    def __init__(self, driver):
        super().__init__(driver)

    def click_off_plan(self):
        self.wait.until(EC.presence_of_element_located(self.OFF_PLAN_BUTTON))
        self.action_click(self.OFF_PLAN_BUTTON)