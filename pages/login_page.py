from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class LoginPage(Base):
    base_url = 'https://www.dns-shop.ru/'

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # Locators
    login_icon = (By.CSS_SELECTOR, ".user-profile__login")
    user_profile = (By.CSS_SELECTOR, ".user-profile__menu")
    button_come_in = (By.CSS_SELECTOR, ".user-profile__guest .base-ui-button_JKH")
    registry_form = (By.CSS_SELECTOR, ".form-entry-or-registry")
    entry_password_form = (By.CSS_SELECTOR, ".form-entry-with-password")
    log_in_with_password = (By.CSS_SELECTOR, ".block-other-login-methods__password-button")
    input_login = (By.XPATH, "//input[@autocomplete='username']")
    input_password = (By.XPATH, "//input[@autocomplete='current-password']")
    button_login = (By.CSS_SELECTOR, ".base-ui-button-v2_big")
    customer_log = (By.CSS_SELECTOR, ".user-menu.user-menu_logged")

    # Actions

    def input_user_name(self, user_name):
        self.get_clickable_element(self.input_login).send_keys(user_name)
        print("input user name")

    def input_user_password(self, user_password):
        self.get_clickable_element(self.input_password).send_keys(user_password)
        print("input user password")

    def click_login_button(self):
        self.get_clickable_element(self.button_login).click()
        print("click login")

    # Methods

    def authorization(self, user_name, user_password):
        """Autorization"""
        self.browser.get(self.base_url)
        self.check_open(self.login_icon)
        self.action.move_to_element(self.browser.find_element(*self.login_icon)).perform()
        self.check_open(self.user_profile)
        self.browser.find_element(*self.button_come_in).click()
        self.get_clickable_element(self.registry_form)
        self.browser.find_element(*self.log_in_with_password).click()
        self.check_open(self.entry_password_form)
        self.input_user_name(user_name)
        self.input_user_password(user_password)
        self.click_login_button()
        self.assert_exist_element(self.customer_log, msg='Customer is not authorized')
        self.get_current_url()
        self.action.click()