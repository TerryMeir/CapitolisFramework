import os


def test_dummy(app_config, browser):
    print(os.environ["BASE_URL"])
    assert True

