from tests.locators.ProductPage import ProductPage as ProductPageLocators
from tests.support.BasePage import BasePage


class ProductPage(BasePage):

    def add_a_product_to_wishlist(self):
        product_page = ProductPageLocators()
        self.element(product_page.add_to_favoirite_button).click()
