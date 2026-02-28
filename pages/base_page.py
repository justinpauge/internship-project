from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_title_contains(self, text):
        self.wait.until(EC.title_contains(text))

    def wait_for_element_present(self, locator):
        self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_element_visible(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_invisible(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))

    def wait_for_staleness(self, element):
        self.wait.until(EC.staleness_of(element))

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element.click()

    def input_text(self, locator, text):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def action_click(self, locator):
        el = self.wait.until(EC.element_to_be_clickable(locator))
        ActionChains(self.driver).move_to_element(el).pause(0.1).click(el).perform()
        return el

    def action_click_visible(self, locator):
        el = self.find_visible(locator)
        ActionChains(self.driver).move_to_element(el).pause(0.1).click(el).perform()
        return el

    def action_send_keys(self, locator, text):
        el = self.find_visible(locator)
        ActionChains(self.driver).move_to_element(el).click(el).pause(0.1).send_keys(text).perform()
        return el

    def press_esc(self):
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
