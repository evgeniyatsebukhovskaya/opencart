class AlertBlock:

    def __init__(self, driver):
        self.driver = driver

    cross_of_alert = './/button[@class="close"]'
    inside_alert_legend = './/legend[text()="Choose how to move the storage directory"]'
