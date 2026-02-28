from behave import given, when, then
import time
time.sleep(5)


@given("User opens the login page")
def open_login(context):
    context.app.login_page.open_login_page()


@when("User logs in")
def login(context):
    context.app.login_page.login("paugevich@gmail.com", "testpassword")
    time.sleep(5)

@when("User clicks on Off-plan in sidebar")
def click_off_plan(context):
    context.app.sidebar.click_off_plan()


@when("User filters by Out of Stock")
def filter_out_of_stock(context):
    context.app.off_plan_page.filter_by_out_of_stock()


@then("All products should have Out of Stock status")
def verify_out_of_stock(context):
    context.app.off_plan_page.verify_first_10_are_out_of_stock()