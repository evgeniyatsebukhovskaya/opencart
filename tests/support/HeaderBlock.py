from tests.locators.HeaderBlock import HeaderBlock as HeaderBlockLocators


class HeaderBlock:

    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        self.driver.find_element_by_xpath(HeaderBlockLocators().logout_button).click()

    def open_profile(self):
        self.driver.find_element_by_xpath(HeaderBlockLocators().menu_button).click()
        self.driver.find_element_by_xpath(HeaderBlockLocators().profile_button).click()

    def check_profile_name(self, name):
        assert self.driver.find_element_by_xpath('.//img[@alt="{}"]'.format(name)).is_displayed()

