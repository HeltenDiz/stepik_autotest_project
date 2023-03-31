from datetime import datetime


class Base:

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        """Method get current url"""
        get_url = self.driver.current_url
        print("Current url " + get_url)

    def assert_word(self, word, result):
        """Method assert word"""
        value_word = word.text
        assert value_word == result
        print("Correct value word")

    def make_screenshot(self):
        """Method make screenshot"""
        now_date = datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot_' + now_date + '.png'
        self.driver.save_screenshot(
            'C:\\Users\\da.boyarincev\\Downloads\\PyProjects\\main_project\\screen' + name_screenshot)

    def assert_url(self, result):
        """Method assert url"""
        get_url = self.driver.current_url
        assert get_url == result
        print("Correct value url")
