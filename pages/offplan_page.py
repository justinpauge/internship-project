import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException



class OffPlanPage(BasePage):

    SALE_STATUS_DROPDOWN = (By.CSS_SELECTOR, "[data-test-id='filter-sale-status-dropdown']")
    OUT_OF_STOCK_OPTION = (By.CSS_SELECTOR, '[data-test-id="filter-badge-out_of_stock"]')
    PRODUCT_STATUSES = (By.CSS_SELECTOR, '[data-test-id="project-card-sale-status"]')

    def __init__(self, driver):
        super().__init__(driver)

    def filter_by_out_of_stock(self):
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located(self.SALE_STATUS_DROPDOWN))
        for attempt in range(3):
            try:
                elements = self.driver.find_elements(*self.SALE_STATUS_DROPDOWN)
                for el in elements:
                    if el.is_displayed():
                        ActionChains(self.driver).move_to_element(el).pause(0.1).click(el).perform()
                        break
                break
            except StaleElementReferenceException:
                time.sleep(0.5)
        self.action_click(self.OUT_OF_STOCK_OPTION)
        self.press_esc()



    def get_first_10_statuses(self):
        # Wait until at least 10 cards are present
        self.wait.until(
            lambda d: len(
                d.find_elements(*self.PRODUCT_STATUSES)
            ) >= 10
        )

        elements = self.driver.find_elements(*self.PRODUCT_STATUSES)[:10]

        print(f"Checking first {len(elements)} statuses")

        return [el.text for el in elements]

    def verify_first_10_are_out_of_stock(self):

        self.wait.until(
            lambda d: len(
                d.find_elements(*self.PRODUCT_STATUSES)
            ) >= 10
        )

        statuses = self.driver.find_elements(*self.PRODUCT_STATUSES)[:10]

        print(f"Verifying first {len(statuses)} results")

        for status in statuses:
            print(f"Status text: {status.text}")
            assert "Out of Stock" in status.text




    def scroll_to_bottom(self):
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.wait.until(lambda d: True)  # small pause via implicit wait

            new_height = self.driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height:
                break

            last_height = new_height

    def find_present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))