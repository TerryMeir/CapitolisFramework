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
        assert True

    def test_dynamic_loading(self, browser):
        dynamic_page = BasePage(browser).click_dynamic_loading()
        dynamic_page.see_hello_world()
        assert True

    def test_jquery_menu(self, browser):
        pass
