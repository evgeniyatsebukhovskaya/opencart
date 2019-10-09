from tests.locators.MainPage import MainPage as MainPageLocators

class MainPage:

    def __init__(self, driver):
        self.driver = driver


    def search_a_product(self, product):
        main_page = MainPageLocators()
        self.driver.find_element_by_xpath(main_page.search_field).send_keys(product)
        self.driver.find_element_by_xpath(main_page.search_button).click()

    def open_all_desktops(self, driver):
        main_page = MainPageLocators()
        driver.find_element_by_xpath(main_page.desktops_button).click()
        driver.find_element_by_link_text(main_page.show_all_desktops).click()
