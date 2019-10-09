from tests.support.LoginPage import LoginPage
from tests.support.NavigationAdminPage import NavigationAdminPage
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
        # login
        driver.get('http://opencart.eng/admin/')
        login_page = LoginPage(driver)
        login_page.login_with_given_data('admin', 'admin')
        alert_block = AlertBlock(driver)
        #close alert
        alert_block.close_alert()
        # Open Products Page
        navigation_page = NavigationAdminPage(driver)
        navigation_page.open_products_page()
        products_page = ProductAdminPage(driver)
        random_product_name = fake.job()
        random_mega_tag = fake.first_name()
        random_model = fake.color_name()
        products_page.create_new_product(random_product_name, random_mega_tag, random_model)
        products_page.check_if_success_message_appears()

    def test_change_quantity_of_product(self, driver):
        # login
        driver.get('http://opencart.eng/admin/')
        login_page = LoginPage(driver)
        login_page.login_with_given_data('admin', 'admin')
        alert_block = AlertBlock(driver)
        alert_block.close_alert()
        # Open Products Page
        navigation_page = NavigationAdminPage(driver)
        navigation_page.open_products_page()
        # Edit first product
        products_page = ProductAdminPage(driver)
        products_page.edit_first_product()
        products_page.check_if_success_message_appears()

    def test_delete_product(self, driver):
        # login
        driver.get('http://opencart.eng/admin/')
        login_page = LoginPage(driver)
        login_page.login_with_given_data('admin', 'admin')
        alert_block = AlertBlock(driver)
        alert_block.close_alert()
        # Open Products Page
        navigation_page = NavigationAdminPage(driver)
        navigation_page.open_products_page()
        # Delete first product
        products_page = ProductAdminPage(driver)
        products_page.delete_first_product()
        products_page.check_if_success_message_appears()








