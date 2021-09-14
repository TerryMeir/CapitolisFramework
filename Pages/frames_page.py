import time

from selenium.webdriver.common.by import By
from HtmlElement import HTMLElement


class FramesPageSelectors:
    IfremeLink = "#content > div > ul > li:nth-child(2) > a"
    IframeInput = "#tinymce > p"


class FramesPage:
    def __init__(self, driver):
        self.driver = driver
        self._iframe_link = HTMLElement(self.driver, by=By.CSS_SELECTOR, locator_value=FramesPageSelectors.IfremeLink)

    def enter_iframe_page(self):
        self._iframe_link.click()

    def send_text(self, txt):
        self.enter_iframe_page()
        iframe = self.driver.find_elements_by_tag_name('iframe')
        self.driver.switch_to.frame(iframe)
        content_box = HTMLElement(self.driver, by=By.CSS_SELECTOR, locator_value=FramesPageSelectors.IframeInput)
        content_box.input_text(txt=txt)
        time.sleep(2)
        self.driver.switch_to.default_content()
