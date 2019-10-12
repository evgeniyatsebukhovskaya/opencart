from tests.support.SearchBlock import SearchBlock
from tests.support.HeaderBlock import HeaderBlock

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.search = SearchBlock(driver)
        self.header = HeaderBlock(driver)

    def element(self, selector: dict):
        by = None
        if 'xpath' in selector.keys():
            by = By.XPATH
            selector = selector['xpath']
        elif 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']
        return self.driver.find_element(by, selector)
