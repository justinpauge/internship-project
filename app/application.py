from pages.login_page import LoginPage

from pages.sidebar import Sidebar
from pages.offplan_page import OffPlanPage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.login_page = LoginPage(self.driver)
        #self.main_page = MainPage(driver)
        self.sidebar = Sidebar(driver)
        self.off_plan_page = OffPlanPage(driver)


