import os
from behave import given, when, then

from pages.login_page import LoginPage
from pages.sidebar import Sidebar
from pages.offplan_page import OffPlanPage
from utils.config import BASE_URL


@given("the user opens the main page")
def step_open_main_page(context):
    context.login_page = LoginPage(context.driver)
    context.sidebar = Sidebar(context.driver)
    context.offplan_page = OffPlanPage(context.driver)

    context.login_page.open(BASE_URL)


@given("the user logs in")
def step_login(context):
    email = os.getenv("REELLY_EMAIL", "paugevich@gmail.com")
    password = os.getenv("REELLY_PASSWORD", "testpassword")
    assert email and password, "Set REELLY_EMAIL and REELLY_PASSWORD environment variables."

    context.login_page.login(email, password)


@when('the user clicks "Off-plan" in the left side menu')
def step_click_offplan(context):
    # After login, this environment often lands directly on find.reelly.io
    # In that case, there is no left menu to click and this step should be treated as already satisfied.
    if "find.reelly.io" in context.driver.current_url:
        print("Already on find.reelly.io, skipping sidebar Off-plan click")
        return

    context.sidebar.go_to_offplan()



@then("the Off-plan page should open")
def step_verify_offplan_opened(context):
    context.offplan_page.assert_opened()


@when('the user filters sale status by "Out of Stock"')
def step_filter_out_of_stock(context):
    context.offplan_page.filter_sale_status_out_of_stock()


@then('every product should contain "Out of Stock"')
def step_verify_all_products_out_of_stock(context):
    context.offplan_page.assert_all_products_out_of_stock()
