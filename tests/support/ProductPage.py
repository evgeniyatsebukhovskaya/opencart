from tests.locators.ProductPage import ProductPage as ProductPageLocators

class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    def add_a_product_to_wishlist(self):
        product_page = ProductPageLocators()
        self.driver.find_element_by_xpath(product_page.add_to_favoirite_button).click()
