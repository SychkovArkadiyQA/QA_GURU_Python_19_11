import pytest
from selene import browser, have, by
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import attach

@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.window_width = 1400
    browser.config.window_height = 1200
    browser.config.base_url = 'https://demoqa.com'

def setup_browser(request):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False}
}
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)



