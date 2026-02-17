import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[type="email"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[type="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".login-button.w-button")

    # Post login anchors (either domain)
    FIND_STATUS_ANCHOR = (By.CSS_SELECTOR, '[data-test-id="filter-sale-status-dropdown"]')
    SOFT_OFFPLAN_ANCHOR = (By.XPATH, '//*[normalize-space()="Off-plan"]')

    def login(self, email: str, password: str):
        self.type(self.EMAIL_INPUT, email)
        self.type(self.PASSWORD_INPUT, password)

        # Try normal click
        self.safe_click(self.LOGIN_BUTTON)

        # Firefox sometimes needs an Enter submit
        try:
            self.wait.until(lambda d: "sign-in" not in d.current_url)
        except TimeoutException:
            pw = self.wait_visible(self.PASSWORD_INPUT)
            pw.send_keys(Keys.ENTER)

        # Now accept either landing:
        # A) redirected to find.reelly.io and we see status filter
        # B) stays on soft.reelly.io but sidebar shows Off-plan
        try:
            self.wait_url_contains("find.reelly.io")
            self.wait_present(self.FIND_STATUS_ANCHOR)
            return
        except TimeoutException:
            pass

        try:
            # still logged in but on soft domain
            self.wait_present(self.SOFT_OFFPLAN_ANCHOR)
            return
        except TimeoutException:
            raise AssertionError(
                "Login did not complete in time on either landing page.\n"
                f"URL: {self.driver.current_url}\n"
                "Expected either find.reelly.io (status filter) or soft.reelly.io (Off-plan in sidebar)."
            )
