from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from stepik_autotest_project.base.base_class import Base


class CartPage(Base):
    base_url = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.cart_price_product = driver.find_elements(By.XPATH,
                                                "//*[@class='sdf']")

    def get_driver(self):
        return self.driver

    # Locators
    # cart_price_product = driver.find_elements(By.XPATH,
    #                                             "//*[@class='inventory_item_price']")  # стоимость товара в корзине
    # checkout = "//button[@id='checkout']"  # кнопка оформления заказа
    # cart_item = get_driver().find_element(By.CSS_SELECTOR, '.cart_item')
    # cart_item_name = get_driver().find_elements(By.CSS_SELECTOR,
    #                                         '.inventory_item_name')  # заголовок названия товара в корзине

    # Getters

    def get_checkout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout)))

    # Actions

    def click_checkout(self):
        self.get_checkout().click()
        print("Click checkout")

    # Methods

    def some(self):
        """"""
