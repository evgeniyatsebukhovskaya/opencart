from tests.locators.LoginPage import LoginPage as LoginPageLocators
from tests.support.BasePage import BasePage
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    def login_with_given_data(self, login, password):
        login_page = LoginPageLocators()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, login_page.user_title['xpath'])))
        self.element(login_page.login_field).send_keys(login)
        self.element(login_page.password_field).send_keys(password)
        self.element(login_page.login_button).click()
