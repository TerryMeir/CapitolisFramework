from basic_test import BasicTest
from Pages.base_page import BasePage


class CapitolisTests(BasicTest):
    def test_checkboxes(self, browser):
        checkboxes_page = BasePage(browser).click_checkboxes()
        checkboxes_page.toggle_checkboxes()
        assert True
