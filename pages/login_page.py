import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from pages.base_page import BasePage


class LoginPage(BasePage):

    EMAIL_FIELD = (By.CSS_SELECTOR, "input[type='email']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[type='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".login-button.w-button")

    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self):
        self.driver.get("https://soft.reelly.io")

    def login(self, email, password):
        time.sleep(4)
        for attempt in range(3):
            try:
                self.action_send_keys(self.EMAIL_FIELD, email)
                break
            except StaleElementReferenceException:
                time.sleep(1)
        time.sleep(0.5)
        for attempt in range(3):
            try:
                self.action_send_keys(self.PASSWORD_FIELD, password)
                break
            except StaleElementReferenceException:
                time.sleep(1)
        time.sleep(1)
        for attempt in range(3):
            try:
                self.action_click(self.LOGIN_BUTTON)
                break
            except StaleElementReferenceException:
                time.sleep(1)
