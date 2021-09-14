from basic_test import BasicTest
from Pages.base_page import BasePage


class CapitolisTests(BasicTest):
    def __init__(self, browser):
        self.driver = browser

    def test_checkboxes(self):
        checkboxes_page = BasePage(self.driver).click_checkboxes()
        checkboxes_page.toggle_checkboxes()
        assert True

    def test_iframe(self):
        frames_page = BasePage(self.driver).click_frames()
        frames_page.send_text("Terry Meir")
        assert True

    def test_dynamic_loading(self):
        dynamic_page = BasePage(self.driver).click_dynamic_loading()
        dynamic_page.see_hello_world()
        assert True

    def test_jquery_menu(self):
        pass

    def test_basic_auth(self):
        pass
