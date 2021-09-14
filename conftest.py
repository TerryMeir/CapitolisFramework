import logging
import json
import os
import time
from dotenv import dotenv_values
from pytest import fixture
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--env", action="store", help="Environment to run tests")  # can add default = "dev"


# scope = function is the lowest scope
# if i will try to create second browser in the same function i will always get the same chrome webdriver (same window)
# higher than function I have scope = session
# in every function i will call this driver i will get always the same webdriver (same window)
# so if i will want to keep the session open from functions that does different actions i need to use 'scope = session'
@fixture(params=[webdriver.Chrome, webdriver.Firefox], scope="session")
def browser(request):
    drvr = request.param
    driver = drvr()
    driver.maximize_window()
    time.sleep(5)
    yield driver
    # teardown
    logging.info(f"I am tearing down {request.param} browser")
    driver.quit()


@fixture(scope='session')
def env(request):
    return request.config.getoption("--env")


@fixture(scope='session')
def app_config(env):
    # logging configuration - remove previous handler and set handler to write to a file
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    logging.basicConfig(filename='automationApp.log', format='%(asctime)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logging.info("____________________________________________APP CONFIG______________________________________________")
    cfg = dotenv_values('.env.' + env)
    logging.info(f"cfg is: {cfg}")
    os.environ.update(cfg)
    logging.info("os.env is:")
    logging.info(json.dumps({**{}, **os.environ}, indent=2))
    return cfg
