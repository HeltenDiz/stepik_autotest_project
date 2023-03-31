from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
import selenium.common.exceptions as selenium_ex


class Base:

    def __init__(self, browser):
        self.browser = browser

    def get_current_url(self):
        """Method get current url"""
        get_url = self.browser.current_url
        print("Current url " + get_url)

    def assert_word(self, word, result):
        """Method assert word"""
        value_word = word.text
        assert value_word == result
        print("Correct value word")

    def check_open(self, locator):
        element = WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable(locator))
        element.is_displayed()

    def is_element_present(self, how, what):
        try:
            element = self.browser.find_element(how, what)
            element.is_displayed()
        except selenium_ex.NoSuchElementException:
            return False
        return True

    def assert_exist_element(self, how, what, msg):
        assert self.is_element_present(how, what), msg

    def get_clickable_element(self, locator):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable(locator))

    def make_screenshot(self):
        """Method make screenshot"""
        now_date = datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot_' + now_date + '.png'
        self.browser.save_screenshot(
            'C:\\Users\\da.boyarincev\\Downloads\\PyProjects\\main_project\\screen' + name_screenshot)

    def assert_url(self, result):
        """Method assert url"""
        get_url = self.browser.current_url
        assert get_url == result
        print("Correct value url")


