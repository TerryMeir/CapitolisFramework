from basic_test import BasicTest
from Pages.base_page import BasePage


class CapitolisTests(BasicTest):
    def test_checkboxes(self, browser):
        checkboxes_page = BasePage(browser).click_checkboxes()
        checkboxes_page.toggle_checkboxes()
        assert True

    def test_basic_auth(self, browser):
        pass

    def test_iframe(self, browser):
        frames_page = BasePage(browser).click_frames()
        frames_page.send_text("Terry Meir")

    def test_dynamic_loading(self, browser):
        pass

    def test_jquery_menu(self, browser):
        pass
