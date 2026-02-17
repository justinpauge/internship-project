from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url: str):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        self.wait_clickable(locator).click()

    def type(self, locator, text: str, clear=True):
        el = self.wait_visible(locator)
        if clear:
            el.clear()
        el.send_keys(text)

    def get_text(self, locator) -> str:
        return self.wait_visible(locator).text

    def all_visible(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def is_visible(self, locator) -> bool:
        try:
            self.wait_visible(locator)
            return True
        except Exception:
            return False

    def safe_click(self, locator):
        el = self.wait_clickable(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)
        try:
            el.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", el)

    def wait_url_contains(self, text: str):
        return self.wait.until(EC.url_contains(text))

    def wait_present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))