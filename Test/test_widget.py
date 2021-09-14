import os
from capitolis_tests import CapitolisTests
from Pages.base_page import BasePage


def test_class(app_config, browser):
    test = CapitolisTests(browser)
    test.test_checkboxes()
    test.test_iframe()
    test.test_dynamic_loading()
    assert True


def test_checkboxes(browser):
    test = CapitolisTests(browser)
    test.test_checkboxes()
    assert True


def test_iframe(browser):
    test = CapitolisTests(browser)
    test.test_iframe()
    assert True


def test_dynamic(browser):
    test = CapitolisTests(browser)
    test.test_dynamic_loading()
    assert True


