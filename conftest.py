import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.ie.options import Options as IeOptions

from pathlib import Path

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="choose chrome, firefox or ie")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument('--headless')
        d = webdriver.Chrome(chrome_options=options)
    if browser == "firefox":
        options = FirefoxOptions()
        options.add_argument('--headless')
        d = webdriver.Firefox(options=options)
    if browser == "ie":
        options = IeOptions()
        options.add_argument('--headless')
        d = webdriver.Ie(options=options)
    d.maximize_window()
    d.get('http://installopencart.localhost/')
    yield d
    d.quit()
    return d

