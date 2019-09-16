class ProductsAdminPage:

    add_new_product_button = './/a[@data-original-title="Add New"]'
    product_name_field = './/input[@placeholder="Product Name"]'
    mega_tag_title_field = './/input[@placeholder="Meta Tag Title"]'
    data_section = './/a[text()="Data"]'
    model_field = './/input[@placeholder="Model"]'
    save_product_button = './/button[@type="submit"]'
    success_message = './/div[@class="alert alert-success alert-dismissible"]'
    edit_first_product_button = '(.//a[@data-original-title="Edit"])[1]'
    quantity_field = './/div[@class="form-group"]//input[@placeholder="Quantity"]'
    select_first_product_selector = '(.//input[@name="selected[]"])[1]'
    delete_button = './/button[@data-original-title="Delete"]'

