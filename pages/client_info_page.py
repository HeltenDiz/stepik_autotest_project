from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class ClientInfoPage(Base):
    base_url = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_driver(self):
        return self.driver

    # Locators

    # first_name = get_driver().find_element(By.XPATH, "//input[@id='first-name']")  # реквизиты: имя
    # last_name = get_driver().find_element(By.XPATH, "//input[@id='last-name']")  # реквизиты: фамилия
    # zip = get_driver().find_element(By.XPATH, "//input[@id='postal-code']")  # почтовый код
    # button_continue = "//input[@id='continue']"  # кнопка продолжения оформления заказа

    # Getters

    def get_button_continue(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_continue)))

    # Actions

    def input_first_name(self, first_name):
        self.first_name.send_keys(first_name)
        print("input first name")

    def input_last_name(self, last_name):
        self.last_name.send_keys(last_name)
        print("input last name")

    def input_zip(self, zip_code):
        self.zip.send_keys(zip_code)
        print("input zip code")

    def click_login_button(self):
        self.get_button_continue().click()
        print("click button continue")

    # Methods

    def input_information(self, first_name, last_name, zip_code):
        """input client information"""
        self.input_first_name(first_name)
        self.input_last_name(last_name)
        self.input_zip(zip_code)
        self.click_login_button()

