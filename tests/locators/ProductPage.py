import pytest
from time import sleep
from selenium import webdriver
from MainPage import MainPage


def driver():
    d = webdriver.Firefox()
    d.maximize_window()
    d.get('http://localhost/opencart/')
    yield d
    d.quit()


class ProductPage():

    add_to_favoirite_button = './/button[@data-original-title="Add to Wish List"]'

class Test_lala():

    def test_add_product_to_wish_list(self, driver):
        product_page = ProductPage()
        main_page = MainPage()
        driver.find_element_by_xpath(main_page.search_field).send_keys("phone")
        driver.find_element_by_xpath(main_page.search_button).click()
        driver.find_element_by_xpath('.//a[text()="iPhone"]').click()
        driver.find_element_by_xpath(product_page.add_to_favoirite_button).click()
        assert driver.find_element_by_xpath('.//a[text()="wish list"]').is_displayed()
