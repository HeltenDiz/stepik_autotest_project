from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from selenium.webdriver import Keys


class ClientCheckoutPage(Base):
    base_url = 'https://www.dns-shop.ru/checkout-main/'

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # Locators

    phone_number = (By.XPATH, "//input[@type='tel']")
    mail = (By.XPATH, "//input[@type='text']")
    pickup_method = (By.XPATH, "//div[contains(text(), 'Самовывоз')]")
    receiving_payment = (By.XPATH, "//div[contains(text(), 'При получении')]")
    apply_order = (By.XPATH, "//span[contains(text(), 'Подтвердить заказ')]")

    # Actions

    def input_phone_number(self, phone_num):
        self.get_clickable_element(self.phone_number).send_keys(phone_num)
        print("input phone")

    def input_mail(self, mail_name):
        input_m = self.get_clickable_element(self.mail)
        input_m.send_keys(Keys.LEFT_CONTROL + Keys.ALT + Keys.DELETE)
        input_m.send_keys(mail_name)
        print("input mail")

    def choose_receiving_method(self, method_name):
        self.browser.find_element(By.XPATH, f"//div[contains(text(), '{method_name}')]")
        print("choose receiving way")

    def choose_payment_method(self, pay_method_name):
        self.browser.find_element(By.XPATH, f"//div[contains(text(), '{pay_method_name}')]")
        print("choose payment way")

    # Methods

    def fill_information_and_confirm(self, phone_num, mail_name, method_name, pay_method_name):
        """input client information"""
        self.check_open(self.apply_order)
        assert self.get_current_url() == self.base_url
        print("Fill in payment and delivery information")
        self.input_phone_number(phone_num)
        self.input_mail(mail_name)
        self.choose_receiving_method(method_name)
        self.choose_payment_method(pay_method_name)
        #self.get_clickable_element(self.apply_order).click()

