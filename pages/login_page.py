from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class LoginPage(Base):
    base_url = 'https://www.computeruniverse.net/'

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # Locators
    login_popup = (By.CLASS_NAME, "[class='c-LoginPopOver__content']")
    username = (By.ID, "[id='login-form_id']")
    password = (By.ID, "[id='login-form_password']")
    button_login = (By.TAG_NAME, "button.at__login__login")
    customer_log = (By.CSS_SELECTOR, "[.customer--logged-in .icon-hook]")

    # Getters

    def get_user_name(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable(self.username))

    def get_user_password(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable(self.password))

    def get_login_button(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable(self.button_login))

    # Actions

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("input user name")

    def input_user_password(self, user_password):
        self.get_user_password().send_keys(user_password)
        print("input user password")

    def click_login_button(self):
        self.get_login_button().click()
        print("click login")

    # Methods

    def authorization(self, user_name, user_password):
        """Autorization"""
        self.check_open(self.login_popup)
        self.input_user_name(user_name)
        self.input_user_password(user_password)
        self.click_login_button()
        self.assert_exist_element(*self.customer_log, msg='Customer is not authorized')
        self.get_current_url()
