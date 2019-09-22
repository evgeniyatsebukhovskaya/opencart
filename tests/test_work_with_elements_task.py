from tests.locators.LoginPage import LoginPage
from tests.locators.NavigationAdminPage import NavigationAdminPage
from tests.locators.ProductsAdminPage import ProductsAdminPage
from tests.locators.AlertBlock import AlertBlock
from time import sleep
from faker import Faker
from faker.providers import internet
from faker.providers import person
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

fake = Faker()
fake.add_provider(internet)
fake.add_provider(person)


class TestProducts:

    def test_create_new_products(self, driver):
        # login
        driver.get('http://opencart.eng/admin/')
        login_page = LoginPage()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, login_page.user_title)))
        driver.find_element_by_css_selector(login_page.login_field).send_keys('admin')
        driver.find_element_by_css_selector(login_page.password_field).send_keys('admin')
        driver.find_element_by_xpath(login_page.login_button).click()
        alert_block = AlertBlock()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, alert_block.inside_alert_legend)))
        driver.find_element_by_xpath(alert_block.cross_of_alert).click()
        # Open Products Page
        navigation_page = NavigationAdminPage()
        driver.find_element_by_xpath(navigation_page.catalog).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, navigation_page.products)))
        driver.find_element_by_xpath(navigation_page.products).click()
        # Open new product creation page
        products_page = ProductsAdminPage()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, products_page.add_new_product_button)))
        driver.find_element_by_xpath(products_page.add_new_product_button).click()
        # Fill information
        random_product_name = fake.job()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, products_page.product_name_field)))
        driver.find_element_by_xpath(products_page.product_name_field).send_keys(random_product_name)
        random_mega_tag = fake.first_name()
        driver.find_element_by_xpath(products_page.mega_tag_title_field).send_keys(random_mega_tag)
        driver.find_element_by_xpath(products_page.data_section).click()
        random_model = fake.color_name()
        driver.find_element_by_xpath(products_page.model_field).send_keys(random_model)
        driver.find_element_by_xpath(products_page.save_product_button).click()
        assert driver.find_element_by_xpath(products_page.success_message).is_displayed()

    def test_change_quantity_of_product(self, driver):
        # login
        driver.get('http://opencart.eng/admin/')
        login_page = LoginPage()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, login_page.user_title)))
        driver.find_element_by_css_selector(login_page.login_field).send_keys('admin')
        driver.find_element_by_css_selector(login_page.password_field).send_keys('admin')
        driver.find_element_by_xpath(login_page.login_button).click()
        alert_block = AlertBlock()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, alert_block.inside_alert_legend)))
        driver.find_element_by_xpath(alert_block.cross_of_alert).click()
        # Open Products Page
        navigation_page = NavigationAdminPage()
        driver.find_element_by_xpath(navigation_page.catalog).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, navigation_page.products)))
        driver.find_element_by_xpath(navigation_page.products).click()
        # Edit first product
        products_page = ProductsAdminPage()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, products_page.add_new_product_button)))
        driver.find_element_by_xpath(products_page.edit_first_product_button).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, products_page.data_section)))
        driver.find_element_by_xpath(products_page.data_section).click()
        driver.find_element_by_xpath(products_page.quantity_field).send_keys(Keys.CONTROL, "a")
        driver.find_element_by_xpath(products_page.quantity_field).send_keys(Keys.BACKSPACE)
        driver.find_element_by_xpath(products_page.quantity_field).send_keys("100")
        driver.find_element_by_xpath(products_page.save_product_button).click()
        assert driver.find_element_by_xpath(products_page.success_message).is_displayed()

    def test_delete_product(self, driver):
        # login
        driver.get('http://opencart.eng/admin/')
        login_page = LoginPage()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, login_page.user_title)))
        driver.find_element_by_css_selector(login_page.login_field).send_keys('admin')
        driver.find_element_by_css_selector(login_page.password_field).send_keys('admin')
        driver.find_element_by_xpath(login_page.login_button).click()
        alert_block = AlertBlock()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, alert_block.inside_alert_legend)))
        driver.find_element_by_xpath(alert_block.cross_of_alert).click()
        # Open Products Page
        navigation_page = NavigationAdminPage()
        driver.find_element_by_xpath(navigation_page.catalog).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, navigation_page.products)))
        driver.find_element_by_xpath(navigation_page.products).click()
        # Delete first product
        products_page = ProductsAdminPage()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, products_page.add_new_product_button)))
        driver.find_element_by_xpath(products_page.select_first_product_selector).click()
        driver.find_element_by_xpath(products_page.delete_button).click()
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to_alert()
        alert.accept()
        assert driver.find_element_by_xpath(products_page.success_message).is_displayed()









