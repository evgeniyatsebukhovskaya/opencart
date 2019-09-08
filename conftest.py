import pytest
from selenium import webdriver
from pathlib import Path

@pytest.fixture
def driver():
    d = webdriver.Firefox()
    d.maximize_window()
    d.get('http://localhost/opencart/')
    yield d
    d.quit()
   # options = webdriver.ChromeOptions()
    #options.add_experimental_option('excludeSwitches', ['enable-logging'])
    #path = Path(__file__).resolve().parent.parent.parent.joinpath('chromedriver.exe')
   # path = Path.cwd() / 'chromedriver.exe'
    #d = webdriver.Chrome(str(path), options=options)
    #d = webdriver.Chrome(str(path), options=options)

   # d.implicitly_wait(10)  # Set the implicitly wait time to 10 seconds
