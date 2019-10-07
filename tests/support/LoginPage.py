from tests.locators.LoginPage import LoginPage as LoginPageLocators
from selenium import webdriver

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def login_with_given_data(self, driver, login, password):
        login_page = LoginPageLocators()
        driver.find_element_by_css_selector(login_page.login_field).send_keys(login)
        driver.find_element_by_css_selector(login_page.password_field).send_keys(password)
        driver.find_element_by_xpath(login_page.login_button).click()
