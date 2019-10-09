from tests.locators.NavigationAdminPage import NavigationAdminPage as NavigationAdminPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class NavigationAdminPage:

    def __init__(self, driver):
        self.driver = driver

    def open_products_page(self):
        navigation_page = NavigationAdminPageLocators()
        self.driver.find_element_by_xpath(navigation_page.catalog).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, navigation_page.products)))
        self.driver.find_element_by_xpath(navigation_page.products).click()
