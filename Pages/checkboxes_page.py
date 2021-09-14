from selenium.webdriver.common.by import By
from HtmlElement import HTMLElement


class CheckboxesPage:
    def __init__(self, driver):
        self.driver = driver
        self._checkboxA = HTMLElement(self.driver, by=By.CSS_SELECTOR, locator_value="#checkboxes > input[type=checkbox]:nth-child(1)")
        self._checkboxB = HTMLElement(self.driver, by=By.CSS_SELECTOR, locator_value="#checkboxes > input[type=checkbox]:nth-child(3)")

    def toggle_checkboxes(self):
        count_of_switching = 0
        count_of_switching = count_of_switching + self._checkboxA.toggle_checkbox()
        count_of_switching = count_of_switching + self._checkboxB.toggle_checkbox()
        if count_of_switching == 2:
            assert True
        else:
            assert False
