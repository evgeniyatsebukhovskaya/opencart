import pytest
from time import sleep
from selenium import webdriver

'''
def driver():
    d = webdriver.Firefox()
    d.maximize_window()
    d.get('http://localhost/opencart/')
    yield d
    d.quit()
    '''

class MainPage():

    header = '#top'
    currency_button = './/form[@id="form-currency"]//button'
    menu_section = '#menu'
    desktops_button = './/a[text()="Desktops"]'
    about_us_button = './/a[text()="About Us"]'
    search_field = './/input[@name="search"]'
    search_button = './/div[@id="search"]//button'

class Test_Page():

    def test_search(self, driver):
        main_page = MainPage()
        driver.find_element_by_xpath(main_page.search_field).send_keys("phone")
        driver.find_element_by_xpath(main_page.search_button).click()
        assert driver.find_element_by_xpath('.//h1[text()="Search - phone"]').is_displayed()

