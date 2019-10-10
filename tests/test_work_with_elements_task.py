from tests.support.LoginPage import LoginPage
from tests.support.NavigationAdminBlock import NavigationAdminBlock
from tests.support.ProductAdminPage import ProductAdminPage
from tests.support.AlertBlock import AlertBlock
from faker import Faker
from faker.providers import internet
from faker.providers import person

fake = Faker()
fake.add_provider(internet)
fake.add_provider(person)


class TestProducts:

    def test_create_new_products(self, driver):
        driver.get('http://opencart.eng/admin/')
        LoginPage(driver).login_with_given_data('admin', 'admin')
        AlertBlock(driver).close_alert()
        NavigationAdminBlock(driver).open_products_page()
        random_product_name = fake.job()
        random_mega_tag = fake.first_name()
        random_model = fake.color_name()
        ProductAdminPage(driver).create_new_product(random_product_name, random_mega_tag, random_model)
        ProductAdminPage(driver).check_if_success_message_appears()

    def test_change_quantity_of_product(self, driver):
        driver.get('http://opencart.eng/admin/')
        LoginPage(driver).login_with_given_data('admin', 'admin')
        AlertBlock(driver).close_alert()
        NavigationAdminBlock(driver).open_products_page()
        ProductAdminPage(driver).edit_first_product()
        ProductAdminPage(driver).check_if_success_message_appears()

    def test_delete_product(self, driver):
        driver.get('http://opencart.eng/admin/')
        LoginPage(driver).login_with_given_data('admin', 'admin')
        AlertBlock(driver).close_alert()
        NavigationAdminBlock(driver).open_products_page()
        ProductAdminPage(driver).delete_first_product()
        ProductAdminPage(driver).check_if_success_message_appears()








