from tests.locators.ProductsAdminPage import ProductsAdminPage as ProductsAdminPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ProductAdminPage:

    def __init__(self, driver):
        self.driver = driver

    def create_new_product(self, product_name, mega_tag, random_model):
        products_page = ProductsAdminPageLocators()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, products_page.add_new_product_button)))
        self.driver.find_element_by_xpath(products_page.add_new_product_button).click()
        # Fill information
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, products_page.product_name_field)))
        self.driver.find_element_by_xpath(products_page.product_name_field).send_keys(product_name)
        self.driver.find_element_by_xpath(products_page.mega_tag_title_field).send_keys(mega_tag)
        self.driver.find_element_by_xpath(products_page.data_section).click()
        self.driver.find_element_by_xpath(products_page.model_field).send_keys(random_model)
        self.driver.find_element_by_xpath(products_page.save_product_button).click()

    def check_if_success_message_appears(self):
        products_page = ProductsAdminPageLocators()
        assert self.driver.find_element_by_xpath(products_page.success_message).is_displayed()

    def edit_first_product(self):
        products_page = ProductsAdminPageLocators()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, products_page.add_new_product_button)))
        self.driver.find_element_by_xpath(products_page.edit_first_product_button).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, products_page.data_section)))
        self.driver.find_element_by_xpath(products_page.data_section).click()
        self.driver.find_element_by_xpath(products_page.quantity_field).send_keys(Keys.CONTROL, "a")
        self.driver.find_element_by_xpath(products_page.quantity_field).send_keys(Keys.BACKSPACE)
        self.driver.find_element_by_xpath(products_page.quantity_field).send_keys("100")
        self.driver.find_element_by_xpath(products_page.save_product_button).click()

    def delete_first_product(self):
        products_page = ProductsAdminPageLocators()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, products_page.add_new_product_button)))
        self.driver.find_element_by_xpath(products_page.select_first_product_selector).click()
        self.driver.find_element_by_xpath(products_page.delete_button).click()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to_alert()
        alert.accept()