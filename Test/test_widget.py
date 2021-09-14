import os

from Pages.base_page import BasePage


def test_dummy(app_config, browser):
    print(os.environ["BASE_URL"])
    BasePage(browser).click_basic_auth()
    assert True

