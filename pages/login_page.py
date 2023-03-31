from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from stepik_autotest_project.base.base_class import Base


class LoginPage(Base):
    base_url = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    username = "//input[@id='user-name']"
    password = "#password"
    button_login = "//input[@value='Login']"
    main_word = "//span[@class='title']"
    result = 'PRODUCTS'

    # Getters

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.username)))

    def get_user_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_login)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

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
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.get_current_url()
        self.input_user_name(user_name)
        self.input_user_password(user_password)
        self.click_login_button()
        #self.assert_word(self.get_main_word, self.result)
