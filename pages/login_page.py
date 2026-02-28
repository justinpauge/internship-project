import time
from selenium.webdriver.common.by import By
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
        time.sleep(2)
        self.action_send_keys(self.EMAIL_FIELD, email)
        time.sleep(0.5)
        self.action_send_keys(self.PASSWORD_FIELD, password)
        time.sleep(0.5)
        self.action_click(self.LOGIN_BUTTON)
