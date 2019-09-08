import pytest
from time import sleep
from pathlib import Path
from selenium import webdriver


class Test():

    def test_one(self):
        #options = webdriver.ChromeOptions()
        #options.add_experimental_option('excludeSwitches', ['enable-logging'])
       # path = Path.cwd() / 'chromedriver.exe'
       # d = webdriver.Chrome(str(path), options=options)
        #d = webdriver.Chrome(executable_path=r'C:\Users\Dmitry\otus2\opencart\chromedriver.exe')
        #d = webdriver.Chrome()
        d = webdriver.Firefox()
        d.maximize_window()
        d.get('http://localhost/opencart/')

        #  sleep(3)
