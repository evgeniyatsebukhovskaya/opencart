from tests.locators.AlertBlock import AlertBlock as AlertBlockLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class AlertBlock:

    def __init__(self, driver):
        self.driver = driver

    def close_alert(self):
        alert_block = AlertBlockLocators()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, alert_block.inside_alert_legend)))
        self.driver.find_element_by_xpath(alert_block.cross_of_alert).click()