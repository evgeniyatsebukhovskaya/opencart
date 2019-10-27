import pytest
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
import time
from time import strftime


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="choose chrome, firefox or ie")
    parser.addoption("--url", action="store", default="http://localopencart/", help="choose your browser")
    parser.addoption("--wait", action="store", default='10', help="set implicitly wait")


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        d = EventFiringWebDriver(webdriver.Chrome(r'C:\Users\QA\opencart\chromedriver'), MyListener())
    if browser == "firefox":
       d = webdriver.Firefox(r'C:\Users\Dmitry\otus2\opencart\geckodriver')
    if browser == "ie":
       d = webdriver.Ie(r'C:\Users\Dmitry\otus2\opencart\IEDriverServer')
    d.maximize_window()
    d.implicitly_wait(request.config.getoption("--wait"))
    d.get(request.config.getoption("--url"))
    yield d
    d.quit()
    return d


class MyListener(AbstractEventListener):

    def before_find(self, by, value, driver):
        # logging.log(msg="Hello, Before find!")
        print(by, value)

    def after_find(self, by, value, driver):
        pass
        #print(by, value, "found")

    def on_exception(self, exception, driver):
        # pass
        time = strftime("%Y-%m-%d-%H-%M")
        driver.save_screenshot('screenshots/'+time+'exception.png')
        #print(exception)

