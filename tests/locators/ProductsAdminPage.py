class ProductsAdminPage:

    add_new_product_button = {'xpath': './/a[@data-original-title="Add New"]'}
    product_name_field = {'xpath': './/input[@placeholder="Product Name"]'}
    mega_tag_title_field = {'xpath': './/input[@placeholder="Meta Tag Title"]'}
    data_section = {'xpath': './/a[text()="Data"]'}
    model_field = {'xpath': './/input[@placeholder="Model"]'}
    save_product_button = {'xpath': './/button[@type="submit"]'}
    success_message = {'xpath': './/div[@class="alert alert-success alert-dismissible"]'}
    edit_first_product_button = {'xpath': '(.//a[@data-original-title="Edit"])[1]'}
    quantity_field = {'xpath': './/div[@class="form-group"]//input[@placeholder="Quantity"]'}
    select_first_product_selector = {'xpath': '(.//input[@name="selected[]"])[1]'}
    delete_button = {'xpath': './/button[@data-original-title="Delete"]'}

