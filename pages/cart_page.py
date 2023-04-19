from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from pages.client_info_page import ClientCheckoutPage


class CartPage(Base):
    base_url = 'https://www.dns-shop.ru/cart/'

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # Locators
    cart_item = (By.CSS_SELECTOR, ".cart-items__product")
    product_price = (By.XPATH, "//span[@class = 'price__current']")
    final_price = (By.CSS_SELECTOR, ".price.summary__price")
    ordering_button = (By.ID, "buy-btn-main")

    # Getters

    def get_order_btn(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable(self.ordering_button))

    # Actions

    def click_to_order(self):
        self.get_order_btn().click()
        print("Click to make order")

    # Methods
    def make_order(self):
        self.click_to_order()
        self.check_open(ClientCheckoutPage(self.browser).apply_order)
        assert self.get_current_url() == ClientCheckoutPage(self.browser).base_url