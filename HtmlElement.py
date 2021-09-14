import logging
import time
from locator import Locator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class HTMLElement(object):

    def __init__(self, driver, **kwargs):
        self.__driver = driver
        logging.info(f"Creat HTMLelement {kwargs}")
        # Data Test ID locator
        if len(kwargs) == 1:
            self.__locator = Locator.get(kwargs["data_test_id"])
            (self.__by_value, self.__locator_value) = self.__locator
        # All other locators
        elif len(kwargs) == 2:
            self.__by_value = kwargs["by"]
            self.__locator_value = kwargs["locator_value"]
            self.__locator = (self.__by_value, self.__locator_value)
        # Invalid input
        else:
            raise Exception("HTMLElement __init__ function: incorrect Locator value, too many kwargs ")
        self._web_elements = self.__find_web_elements()
        if len(self._web_elements) == 1:
            self._web_element = self._web_elements[0]
        else:
            self._web_element = None

    def __find_web_elements(self):
        """
        finds all elements
        """
        element = WebDriverWait(self.__driver, 10).until(ec.presence_of_all_elements_located(locator=self.__locator))
        return element

    def click(self):
        # print(f"_web element = {self._web_element} type is: {type(self._web_element)}")
        self._web_element.click()

    def input_text(self, txt):
        # wait for the element to be active
        time.sleep(1)
        self._web_element.send_keys(txt)

    @property
    def text(self):
        txt = self._web_element.text
        return txt
