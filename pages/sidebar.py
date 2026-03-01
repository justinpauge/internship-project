import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from pages.base_page import BasePage


class Sidebar(BasePage):

    OFF_PLAN_BUTTON = (By.XPATH, "//button[contains(., 'Off')]")

    def __init__(self, driver):
        super().__init__(driver)

    def click_off_plan(self):
        time.sleep(3)
        long_wait = WebDriverWait(self.driver, 30)
        long_wait.until(EC.presence_of_element_located(self.OFF_PLAN_BUTTON))
        for attempt in range(3):
            try:
                self.action_click(self.OFF_PLAN_BUTTON)
                break
            except StaleElementReferenceException:
                time.sleep(1)