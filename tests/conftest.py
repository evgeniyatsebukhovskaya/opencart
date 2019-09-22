import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="choose chrome, firefox or ie")
    parser.addoption("--url", action="store", default="http://opencart.eng/", help="choose your browser")
   #parser.addoption("--wait", action="store", default='10', help="set implicitly wait")

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        d = webdriver.Chrome(r'C:\Users\Dmitry\otus2\opencart\chromedriver')
    if browser == "firefox":
        d = webdriver.Firefox(r'C:\Users\Dmitry\otus2\opencart\geckodriver')
    if browser == "ie":
        d = webdriver.Ie(r'C:\Users\Dmitry\otus2\opencart\IEDriverServer')
    d.maximize_window()
    d.implicitly_wait(10)
    d.get(request.config.getoption("--url"))
    yield d
    d.quit()
    return d
