from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains

@pytest.fixture
def driver():
    d = webdriver.Chrome(r'C:\Users\Dmitry\otus2\opencart\chromedriver')
    d.maximize_window()
    yield d
    d.quit()
    return d


class TestDragAndDrop:

    def test_put_icons_in_basket(self, driver):
        driver.get('https://marcojakob.github.io/dart-dnd/basic/')
        basket = driver.find_element_by_xpath('.//div[@class="container"]/div')
        icons = driver.find_elements_by_xpath('.//img')
        action_chains = ActionChains(driver)
        action_chains.drag_and_drop(icons[0], basket).drag_and_drop(icons[1], basket).drag_and_drop(icons[2], basket).\
            drag_and_drop(icons[3], basket).perform()
        sleep(3)

