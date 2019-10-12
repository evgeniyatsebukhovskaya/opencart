class MainPage:

    header = {'css': '#top'}
    currency_button = {'xpath': './/form[@id="form-currency"]//button'}
    menu_section = {'css': '#menu'}
    desktops_button = {'xpath': './/a[text()="Desktops"]'}
    about_us_button = {'xpath': './/a[text()="About Us"]'}
    show_all_desktops = {'xpath': './/a[text()="Show All Desktops"]'}
    add_to_cart_first_product = {'xpath': '(.//button/span[text()="Add to Cart"])[1]'}
    no_items_are_added_to_cart = {'xpath': './/span[text()[contains(.," 0 item(s)")] ]'}
    one_item_is_added_to_cart = {'xpath': './/span[text()[contains(.," 1 item(s)")] ]'}
    two_items_are_added_to_cart = {'xpath': './/span[text()[contains(.," 2 item(s)")] ]'}
    cart = {'xpath': './/div[@id="cart"]/button'}
    message_cart_is_empty = {'xpath': './/p[text()="Your shopping cart is empty!"]'}
