from tests.locators.SearchBlock import SearchBlock as SearchBlockLocators

class SearchBlock:

    def __init__(self, driver):
        self.driver = driver

    def search_a_product(self, product):
        search_block = SearchBlockLocators()
        self.driver.find_element_by_xpath(search_block.search_field).send_keys(product)
        self.driver.find_element_by_xpath(search_block.search_button).click()

