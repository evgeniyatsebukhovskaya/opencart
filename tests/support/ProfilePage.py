from tests.locators.ProfilePage import ProfilePage as ProfilePageLocators
from tests.support.BasePage import BasePage
from selenium.webdriver.common.keys import Keys


class ProfilePage(BasePage):

    def change_name(self, new_first_name, new_last_name):
        self.element(ProfilePageLocators().first_name_field).send_keys(Keys.CONTROL, "a")
        self.element(ProfilePageLocators().first_name_field).send_keys(Keys.BACKSPACE)
        self.element(ProfilePageLocators().first_name_field).send_keys(new_first_name)
        self.element(ProfilePageLocators().last_name_field).send_keys(Keys.CONTROL, "a")
        self.element(ProfilePageLocators().last_name_field).send_keys(Keys.BACKSPACE)
        self.element(ProfilePageLocators().last_name_field).send_keys(new_last_name)
        self.element(ProfilePageLocators().save_button).click()
