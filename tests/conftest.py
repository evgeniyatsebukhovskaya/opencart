import pytest
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from time import strftime
import inspect
import logging


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="choose chrome, firefox or ie")
    parser.addoption("--url", action="store", default="http://localopencart/", help="choose your browser")
    parser.addoption("--wait", action="store", default='10', help="set implicitly wait")


@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('w3c', False)
    #wd = webdriver.Chrome(chrome_options=options)
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        d = EventFiringWebDriver(webdriver.Chrome(r'C:\Users\QA\opencart\chromedriver', chrome_options=options), MyListener())
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


date = strftime("%Y-%m-%d-%H-%M")
logging.basicConfig(filename=date + "_access.log", level=logging.INFO)

# создаём консольный handler и задаём уровень
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# создаём formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# добавляем formatter в ch
ch.setFormatter(formatter)


class MyListener(AbstractEventListener):

    def before_find(self, by, value, driver):
        logging.log(logging.INFO, msg="Before find! " + by + ' ' + value)

    def after_find(self, by, value, driver):
        logging.log(logging.INFO, msg=by + ' ' + value + "is found")

    def on_exception(self, exception, driver):
        print(driver.log_types)
        for l in driver.get_log("browser"):
            print(l)
        date = strftime("%Y-%m-%d-%H-%M")
        name = inspect.stack()[5][3]
        driver.save_screenshot('screenshots/' + date + ' ' + name + '.png')

