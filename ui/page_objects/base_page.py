import time

from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class DemoQA:
    base_url: str = 'https://demoqa.com/'

    def __init__(self, driver, path):
        self.driver = driver
        self.base_url += path

    def find_element(self, locator, element=False, time=10):
        message = f"Can't find element by locator {locator}"
        _element = element if element else self.driver
        return WebDriverWait(_element, time).until(EC.presence_of_element_located(locator), message=message)

    def find_elements(self, locator, element=False, time=10):
        message = f"Can't find element by locator {locator}"
        _element = element if element else self.driver
        return WebDriverWait(_element, time).until(EC.presence_of_all_elements_located(locator), message=message)

    def scroll_to_element(self, elem):
        return self.driver.execute_script("return arguments[0].scrollIntoView(true);", elem)

    def select_element(self, elem, item):
        select = Select(elem)
        select.select_by_visible_text(item)

    def select_element_react(self, elem, item):
        elem.send_keys(item)
        time.sleep(0.1)
        elem.send_keys(Keys.ENTER)

    def go_to_site(self):
        return self.driver.get(self.base_url)
