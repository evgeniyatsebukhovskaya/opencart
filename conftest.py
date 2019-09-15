import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.ie.options import Options as IeOptions

from pathlib import Path

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="choose chrome, firefox or ie")
    parser.addoption("--url", action="store", default="http://installopencart.localhost/", help="choose your browser")


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument('--headless')
        d = webdriver.Chrome(options=options)
    if browser == "firefox":
        options = FirefoxOptions()
        options.add_argument('--headless')
        d = webdriver.Firefox(options=options)
    if browser == "ie":
        options = IeOptions()
        options.add_argument('--headless')
        d = webdriver.Ie(options=options)
    d.maximize_window()
    #d.get('http://installopencart.localhost/')
    d.get(request.config.getoption("--url"))
    yield d
    d.quit()
    return d

