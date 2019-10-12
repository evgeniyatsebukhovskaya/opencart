from tests.support.LoginPage import LoginPage
from tests.support.NavigationAdminBlock import NavigationAdminBlock
from tests.support.ProductAdminPage import ProductAdminPage
from tests.support.AlertBlock import AlertBlock
from tests.support.ProfilePage import ProfilePage
from faker import Faker
from faker.providers import internet
from faker.providers import person
from time import sleep

fake = Faker()
fake.add_provider(internet)
fake.add_provider(person)


class TestAdmin:

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

    def test_logout(self, driver):
        driver.get('http://opencart.eng/admin/')
        LoginPage(driver).login_with_given_data('admin', 'admin')
        AlertBlock(driver).close_alert()
        NavigationAdminBlock(driver).header.logout()
        LoginPage(driver).check_user_at_login_page()

    def test_change_admin_name(self, driver):
        driver.get('http://opencart.eng/admin/')
        LoginPage(driver).login_with_given_data('admin', 'admin')
        AlertBlock(driver).close_alert()
        NavigationAdminBlock(driver).header.open_profile()
        new_first_name = fake.first_name()
        new_last_name = fake.last_name()
        new_name = new_first_name+' '+new_last_name
        ProfilePage(driver).change_name(new_first_name, new_last_name)
        ProfilePage(driver).header.check_profile_name(new_name)








