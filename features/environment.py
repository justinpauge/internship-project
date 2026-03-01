from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from app.application import Application


def browser_init(context):
    browser = context.config.userdata.get('browser', 'chrome').lower()
    headless = context.config.userdata.get('headless', 'false').lower() == 'true'

    if browser == 'browserstack':
        options = ChromeOptions()
        options.set_capability('bstack:options', {
            'os': 'OS X',
            'osVersion': 'Sonoma',
            'browserVersion': 'latest',
            'userName': 'justinpauge_qhkxd8',
            'accessKey': 'x6TYFphAbqbRTifYNPqr',
            'sessionName': 'Out of Stock Filter Test',
        })
        context.driver = webdriver.Remote(
            command_executor='https://hub-cloud.browserstack.com/wd/hub',
            options=options,
        )
    elif browser == 'browserstack_mobile':
        options = ChromeOptions()
        options.set_capability('bstack:options', {
            'osVersion': '17',
            'deviceName': 'iPhone 15',
            'userName': 'justinpauge_qhkxd8',
            'accessKey': 'x6TYFphAbqbRTifYNPqr',
            'sessionName': 'Out of Stock Mobile Test',
        })
        context.driver = webdriver.Remote(
            command_executor='https://hub-cloud.browserstack.com/wd/hub',
            options=options,
        )
    elif browser == 'mobile':
        mobile_emulation = {
            "deviceName": "iPhone 12 Pro"
        }
        options = ChromeOptions()
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        if headless:
            options.add_argument('--headless')
        context.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
    elif browser == 'firefox':
        options = FirefoxOptions()
        if headless:
            options.add_argument('--headless')
            options.add_argument('--width=1920')
            options.add_argument('--height=1080')
        context.driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )
    else:
        options = ChromeOptions()
        if headless:
            options.add_argument('--headless')
            options.add_argument('--window-size=1920,1080')
        context.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )

    if browser not in ('mobile', 'browserstack_mobile'):
        context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario:', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step:', step.name)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed:', step.name)
        context.driver.save_screenshot(f"failed_{step.name}.png")
        browser = context.config.userdata.get('browser', 'chrome').lower()
        if browser not in ('browserstack', 'browserstack_mobile'):
            print("Step failed. Pausing browser for inspection...")
            input("Press Enter to close browser...")

def after_scenario(context, scenario):
    browser = context.config.userdata.get('browser', 'chrome').lower()
    if browser in ('browserstack', 'browserstack_mobile'):
        if scenario.status == 'passed':
            context.driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status": "passed", "reason": "All steps passed"}}'
            )
        else:
            context.driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status": "failed", "reason": "Test failed"}}'
            )
    context.driver.quit()
