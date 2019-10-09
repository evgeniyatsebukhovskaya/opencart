from tests.locators.LoginPage import LoginPage as LoginPageLocators
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def login_with_given_data(self, login, password):
        login_page = LoginPageLocators()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, login_page.user_title)))
        self.driver.find_element_by_css_selector(login_page.login_field).send_keys(login)
        self. driver.find_element_by_css_selector(login_page.password_field).send_keys(password)
        self.driver.find_element_by_xpath(login_page.login_button).click()
