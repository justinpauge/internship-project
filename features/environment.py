print("ENVIRONMENT.PY LOADED")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def before_scenario(context, scenario):
    browser = context.config.userdata.get("browser", "chrome").lower()

    if browser == "firefox":
        print("Starting Firefox browser")
        options = webdriver.FirefoxOptions()
        options.set_preference("browser.privatebrowsing.autostart", True)
        options.set_preference("signon.rememberSignons", False)

        service = FirefoxService(GeckoDriverManager().install())
        context.driver = webdriver.Firefox(service=service, options=options)

    else:
        print("Starting Chrome browser")
        service = ChromeService(ChromeDriverManager().install())
        context.driver = webdriver.Chrome(service=service)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)


def before_step(context, step):
    print("\nStarted step:", step)


def after_step(context, step):
    print(f"STEP RESULT: {step.keyword}{step.name} -> {step.status}")
    if step.exception:
        print("STEP EXCEPTION:", repr(step.exception))
    try:
        print("CURRENT URL:", context.driver.current_url)
    except Exception:
        pass


def after_scenario(context, scenario):
    context.driver.quit()
