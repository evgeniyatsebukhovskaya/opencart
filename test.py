import pytest
from time import sleep

class Test:

    def test_opencart_is_opened(self, driver):
        assert driver.find_element_by_xpath('.//a[contains(text(), "Opencart")]').is_displayed()








