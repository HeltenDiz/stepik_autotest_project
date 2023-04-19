from datetime import datetime

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
import selenium.common.exceptions as selenium_ex
import re


class Base:

    def __init__(self, browser):
        self.browser = browser
        self.action = ActionChains(browser)

    def get_current_url(self):
        """Method get current url"""
        get_url = self.browser.current_url
        print("Current url " + get_url)
        return get_url

    def read_title(self, element):
        """Метод возвращает текст элемента"""
        value_text = element.text
        return value_text

    def leave_numbers_1(self, string):
        """Метод возвращает вещественные числа из строки"""

        nums = re.findall(r'\d*\.\d+|\d+', string)
        if nums:
            nums = float(nums[0])

        print(nums)
        return nums

    def leave_numbers_2(self, string):
        """Метод возвращает вещественные числа из строки"""

        nums = ''
        for i in string:
            if i.isdigit() or i == '.':
                nums = nums + i
        print(nums)
        return nums

    def read_price(self, locator, num):
        element_price = self.browser.find_elements(*locator)[num]
        price = self.read_title(element_price)
        price = self.leave_numbers_2(price)
        return price

    def get_len_elements(self, locator):
        elements = self.browser.find_elements(*locator)
        len_elements = len(elements)
        return len_elements


    def assert_word(self, word, result):
        """Method assert word"""
        value_word = word.text
        assert value_word == result
        print("Correct value of word in element")

    def check_open(self, locator):
        element = WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable(locator))
        element.is_displayed()
        print("Page element loaded")

    def is_element_present(self, locator):
        try:
            element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(locator))
            element.is_displayed()
        except (selenium_ex.NoSuchElementException, selenium_ex.TimeoutException):
            return False
        return True

    def is_composite_locator_present(self, descendant, second_locator):
        try:
            element = WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable(descendant.find_element(By.CSS_SELECTOR, second_locator)))
            element.is_displayed()
        except selenium_ex.NoSuchElementException:
            return False
        return True

    def assert_exist_element(self, locator, msg):
        assert self.is_element_present(locator), msg

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

    def check_load_img(self, image_file):
        self.browser.execute_script(
            "return arguments[0].complete && typeof arguments[0].naturalWidth != \"undefined\" && arguments[0].naturalWidth > 0",
            image_file);


