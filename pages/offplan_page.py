from time import sleep

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class OffPlanPage(BasePage):
    STATUS_BUTTON = (By.CSS_SELECTOR, '[data-test-id="filter-sale-status-dropdown"]')
    OUT_OF_STOCK_OPTION = (By.CSS_SELECTOR, '[data-test-id="filter-badge-out_of_stock"]')

    def assert_opened(self):
        self.wait_url_contains("find.reelly.io")

        # Presence is less strict than visibility/clickable
        try:
            self.wait_present(self.STATUS_BUTTON)
        except TimeoutException:
            raise AssertionError(
                "On find.reelly.io but status dropdown was not found in DOM.\n"
                f"URL: {self.driver.current_url}\n"
                'Expected: [data-test-id="filter-sale-status-dropdown"]'
            )

    def safe_click(self, locator):
        el = self.wait_clickable(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)
        try:
            ActionChains(self.driver).move_to_element(el).pause(0.1).click(el).perform()
        except Exception:
            self.driver.execute_script("arguments[0].click();", el)


    def filter_sale_status_out_of_stock(self):
        # Wait until at least 1 status dropdown exists
        self.wait.until(EC.presence_of_all_elements_located(self.STATUS_BUTTON))

        elements = self.find_elements(*self.STATUS_BUTTON)

        # Prefer the first *displayed* element instead of hardcoding index 1
        status_el = None
        for el in elements:
            if el.is_displayed() and el.is_enabled():
                status_el = el
                break

        if status_el is None:
            raise AssertionError("Found status dropdown elements, but none were clickable/displayed.")

        # Click status dropdown (use JS fallback if normal click is flaky)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", status_el)
        try:
            status_el.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", status_el)

        # Now wait for Out of Stock option and click it
        self.wait.until(EC.element_to_be_clickable(self.OUT_OF_STOCK_OPTION))
        self.safe_click(self.OUT_OF_STOCK_OPTION)
