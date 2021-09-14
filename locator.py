from selenium.webdriver.common.by import By


class Locator:
    @staticmethod
    def get(data_test_id):
        locator = '[data-test-id = "'+data_test_id+'"]'
        by = By.CSS_SELECTOR
        return by, locator
