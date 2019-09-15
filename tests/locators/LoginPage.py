import pytest
from time import sleep
from selenium import webdriver
from MainPage import MainPage

'''
def driver():
    d = webdriver.Firefox()
    d.maximize_window()
    d.get('http://localhost/opencart/')
    yield d
    d.quit()
'''

class LoginPage():
    login_field = '#input-username'
    password_field = '#input-password'
    login_button = './/button[@type="submit"]'

    def login_as(self, login, password, driver):
        driver.find_element_by_css_selector(self.login_field).send_keys(login)
        driver.find_element_by_css_selector(self.password_field).send_keys(password)
        driver.find_element_by_xpath(self.login_button).click()

class Test_ololo():

    def test_login_with_incorrect_data(self):
        d = webdriver.Firefox()
        d.maximize_window()
        d.get('http://localhost/opencart/admin/')
        login_page = LoginPage()
        login_page.login_as('test@test.com', '123456', d)
        assert d.find_element_by_xpath('.//div[@class="alert alert-danger alert-dismissible"]').is_displayed()
        d.quit()

    def test_login_with_correct_data(self):
        d = webdriver.Firefox()
        d.maximize_window()
        d.get('http://localhost/opencart/admin/')
        login_page = LoginPage()
        login_page.login_as('admin', 'admin', d)
        assert d.find_element_by_xpath('.//span[text()="Logout"]').is_displayed()
        d.quit()

