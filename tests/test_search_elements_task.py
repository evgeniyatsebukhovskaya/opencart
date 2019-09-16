import pytest
from selenium import webdriver
from tests.locators.MainPage import MainPage
from tests.locators.LoginPage import LoginPage
from tests.locators.ProductPage import ProductPage
from time import sleep


class TestSearchElement:

    def test_login_with_incorrect_data(self, driver):
        driver.get('http://opencart.eng/admin/')
        login_page = LoginPage()
        driver.find_element_by_css_selector(login_page.login_field).send_keys('test@test.com')
        driver.find_element_by_css_selector(login_page.password_field).send_keys('123456')
        driver.find_element_by_xpath(login_page.login_button).click()
        assert driver.find_element_by_xpath('.//div[@class="alert alert-danger alert-dismissible"]').is_displayed()

    def test_login_with_correct_data(self, driver):
        driver.get('http://opencart.eng/admin/')
        login_page = LoginPage()
        driver.find_element_by_css_selector(login_page.login_field).send_keys('admin')
        driver.find_element_by_css_selector(login_page.password_field).send_keys('admin')
        driver.find_element_by_xpath(login_page.login_button).click()
        assert driver.find_element_by_xpath('.//span[text()="Logout"]').is_displayed()

    def test_search(self, driver):
        main_page = MainPage()
        driver.find_element_by_xpath(main_page.search_field).send_keys("phone")
        driver.find_element_by_xpath(main_page.search_button).click()
        assert driver.find_element_by_xpath('.//h1[text()="Search - phone"]').is_displayed()

    def test_open_all_desktops(self, driver):
        main_page = MainPage()
        driver.find_element_by_xpath(main_page.desktops_button).click()
        driver.find_element_by_link_text(main_page.show_all_desktops).click()
        assert driver.find_element_by_xpath('.//a[text()="Desktops (13)"]').is_displayed()

    def test_add_product_to_wish_list(self, driver):
        product_page = ProductPage()
        main_page = MainPage()
        driver.find_element_by_xpath(main_page.search_field).send_keys("phone")
        driver.find_element_by_xpath(main_page.search_button).click()
        driver.find_element_by_xpath('.//a[text()="iPhone"]').click()
        driver.find_element_by_xpath(product_page.add_to_favoirite_button).click()
        sleep(1)
        assert driver.find_element_by_xpath('.//a[text()="wish list"]').is_displayed()