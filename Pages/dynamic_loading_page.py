from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from HtmlElement import HTMLElement


class DynamicLoadingSelector:
    ExampleB = "#content > div > a:nth-child(8)"
    StartButton = "#start > button"
    HelloWorld = "#finish > h4"


class DynamicLoadingPage:
    def __init__(self, driver):
        self.driver = driver
        self._example_b_button = HTMLElement(self.driver, by=By.CSS_SELECTOR, locator_value=DynamicLoadingSelector.ExampleB)

    def see_hello_world(self):
        self._example_b_button.click()
        HTMLElement(self.driver, by=By.CSS_SELECTOR, locator_value=DynamicLoadingSelector.StartButton).click()
        hello_world_element = WebDriverWait(self.driver, 30).until(ec.presence_of_element_located((By.CSS_SELECTOR, DynamicLoadingSelector.HelloWorld)))
        if hello_world_element.text == "Hello World!":
            assert True
