import pytest
from selenium import webdriver
from tests.support.MainPage import MainPage
from tests.support.ProductPage import ProductPage
from tests.support.LoginPage import LoginPage
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestSearchElement:

    def test_login_with_incorrect_data(self, driver):
        driver.get('http://opencart.eng/admin/')
        login_page = LoginPage(driver)
        login_page.login_with_given_data('test@test.com', '123456')
        assert driver.find_element_by_xpath('.//div[@class="alert alert-danger alert-dismissible"]').is_displayed()

    def test_login_with_correct_data(self, driver):
        driver.get('http://opencart.eng/admin/')
        login_page = LoginPage(driver)
        login_page.login_with_given_data('admin', 'admin')
        assert driver.find_element_by_xpath('.//span[text()="Logout"]').is_displayed()

    def test_search(self, driver):
        main_page = MainPage(driver)
        main_page.search_a_product('phone')
        assert driver.find_element_by_xpath('.//h1[text()="Search - phone"]').is_displayed()

    def test_open_all_desktops(self, driver):
        main_page = MainPage(driver)
        main_page.open_all_desktops(driver)
        assert driver.find_element_by_xpath('.//a[text()="Desktops (13)"]').is_displayed()

    def test_add_product_to_wish_list(self, driver):
        product_page = ProductPage(driver)
        main_page = MainPage(driver)
        main_page.search_a_product('phone')
        driver.find_element_by_xpath('.//a[text()="iPhone"]').click()
        product_page.add_a_product_to_wishlist()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, './/a[text()="wish list"]')))
        assert driver.find_element_by_xpath('.//a[text()="wish list"]').is_displayed()
