import os
from pages.login_page import LoginPage
from pages.sidebar import Sidebar
from pages.offplan_page import OffPlanPage
from utils.config import BASE_URL


def test_user_can_filter_by_out_of_stock(driver):
    # Credentials: set these in your OS env vars (recommended for Jira projects)
    email = os.getenv("REELLY_EMAIL", "")
    password = os.getenv("REELLY_PASSWORD", "")
    assert email and password, "Set REELLY_EMAIL and REELLY_PASSWORD environment variables."

    login = LoginPage(driver)
    sidebar = Sidebar(driver)
    offplan = OffPlanPage(driver)

    # 1 Open main page
    login.open(BASE_URL)

    # 2 Log in
    login.login(email, password)

    # 3 Click Off-plan in left menu
    sidebar.go_to_offplan()

    # 4 Verify right page opens
    offplan.assert_opened()

    # 6 Filter by sale status Out of Stock
    offplan.filter_sale_status_out_of_stock()

    # 7 Verify each product contains Out of Stock
    offplan.assert_all_products_out_of_stock()
