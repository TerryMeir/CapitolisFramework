import os
from selenium.webdriver.common.by import By

from Pages.basic_auth_page import BasicAuthPage
from Pages.checkboxes_page import CheckboxesPage
from Pages.dynamic_loading_page import DynamicLoadingPage
from Pages.frames_page import FramesPage
from Pages.jqueryUI_menu import JqueryUiMenuPage
from Pages.page import Page
from HtmlElement import HTMLElement


class BasePageSelector:
    BasicAuthPageLink = "#content > ul > li:nth-child(3) > a"
    CheckboxesPageLink = "#content > ul > li:nth-child(6) > a"
    DynamicLoadingPageLink = "#content > ul > li:nth-child(14) > a"
    FramesPageLink = "#content > ul > li:nth-child(22) > a"
    JqueryUImenuLink = "#content > ul > li:nth-child(28) > a"


class BasePage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = os.environ["BASE_URL"]
        self.go()
        print("Construct Base-Page (Homepage)")
        self.__build_elements()

    def __build_elements(self):
        self._basic_auth = HTMLElement(self.driver, by=By.CSS_SELECTOR, locator_value=BasePageSelector.BasicAuthPageLink)
        self._checkboxes = HTMLElement(self.driver, by=By.CSS_SELECTOR, locator_value=BasePageSelector.CheckboxesPageLink)
        self._dynamic_loading = HTMLElement(self.driver, by=By.CSS_SELECTOR, locator_value=BasePageSelector.DynamicLoadingPageLink)
        self._frames = HTMLElement(self.driver, by=By.CSS_SELECTOR, locator_value=BasePageSelector.FramesPageLink)
        self._jquery_ui_menu = HTMLElement(self.driver, by=By.CSS_SELECTOR, locator_value=BasePageSelector.JqueryUImenuLink)

    def click_basic_auth(self):
        self._basic_auth.click()
        return BasicAuthPage(self.driver)

    def click_checkboxes(self):
        self._checkboxes.click()
        return CheckboxesPage(self.driver)

    def click_dynamic_loading(self):
        self._dynamic_loading.click()
        return DynamicLoadingPage(self.driver)

    def click_frames(self):
        self._frames.click()
        return FramesPage(self.driver)

    def click_jquery_ui_menu(self):
        self._jquery_ui_menu.click()
        return JqueryUiMenuPage(self.driver)
