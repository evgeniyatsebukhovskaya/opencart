from selenium import webdriver


class MainPage:

    header = '#top'
    currency_button = './/form[@id="form-currency"]//button'
    menu_section = '#menu'
    desktops_button = './/a[text()="Desktops"]'
    about_us_button = './/a[text()="About Us"]'
    search_field = './/input[@name="search"]'
    search_button = './/div[@id="search"]//button'
    show_all_desktops = 'Show All Desktops'
