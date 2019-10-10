from tests.locators.NavigationAdminBlock import NavigationAdminBlock as NavigationAdminBlockLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from tests.support.BasePage import BasePage


class NavigationAdminBlock(BasePage):

    def open_products_page(self):
        navigation_page = NavigationAdminBlockLocators()
        self.element(navigation_page.catalog).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, navigation_page.products['xpath'])))
        self.element(navigation_page.products).click()
