from tests.locators.MainPage import MainPage as MainPageLocators
from tests.support.BasePage import BasePage

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    def open_all_desktops(self):
        main_page = MainPageLocators()
        self.element(main_page.desktops_button).click()
        self.element(main_page.show_all_desktops).click()

    def add_first_product_to_cart(self):
        self.element(MainPageLocators().add_to_cart_first_product).click()

    def check_one_item_is_added_to_cart(self):
        assert self.element(MainPageLocators().one_item_is_added_to_cart).is_displayed()

    def check_two_items_are_added_to_cart(self):
        assert self.element(MainPageLocators().two_items_are_added_to_cart).is_displayed()

    def check_no_items_are_added_to_cart(self):
        assert self.element(MainPageLocators().no_items_are_added_to_cart).is_displayed()

    def open_cart(self):
        self.element(MainPageLocators().cart).click()

    def check_cart_is_empty(self):
        assert self.element(MainPageLocators().message_cart_is_empty).is_displayed()

