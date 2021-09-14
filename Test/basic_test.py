import pytest


@pytest.mark.usefixtures("app_config", "browser")
class BasicTest:
    pass
