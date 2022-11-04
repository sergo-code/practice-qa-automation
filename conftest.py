import os
import pytest

from ui.driver import BrowserInterface
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")
    parser.addoption("--browser_version", action="store", default="106.0")
    parser.addoption("--hub", action="store", default="192.168.1.102")
    parser.addoption("--hub_port", action="store", default="4444")
    parser.addoption("--enable_vnc", action="store", default="false")
    parser.addoption("--local", action="store", default="false")


@pytest.fixture()
def browser(request):
    if request.config.getoption('local') == 'false':
        driver = BrowserInterface(request.config)
        yield driver.driver
        driver.quit()
    else:
        service = Service(executable_path=os.path.join(os.getcwd(), 'chromedriver'))
        driver = webdriver.Chrome(service=service)
        yield driver
        driver.quit()
