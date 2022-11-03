import pytest

from ui.driver import BrowserInterface


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")
    parser.addoption("--browser_version", action="store", default="106.0")
    parser.addoption("--hub", action="store", default="192.168.1.102")
    parser.addoption("--hub_port", action="store", default="4444")
    parser.addoption("--enable_vnc", action="store", default="false")


@pytest.fixture()
def browser(request):
    driver = BrowserInterface(request.config)
    yield driver.driver
    driver.quit()
    