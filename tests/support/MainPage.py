from tests.locators.MainPage import MainPage as MainPageLocators
from tests.support.BasePage import BasePage


class MainPage(BasePage):

    def open_all_desktops(self):
        main_page = MainPageLocators()
        self.element(main_page.desktops_button).click()
        self.element(main_page.show_all_desktops).click()
