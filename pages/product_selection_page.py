import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import CartPage
from pages.main_page import MainPage


class ProductSelectionPage(MainPage):
    base_url = 'https://www.dns-shop.ru/'

    # Locators
    image_file = (By.CSS_SELECTOR, ".ais-Hits-item .ProductListItemRow_imgBox__WUReP img")
    section_name = (By.CSS_SELECTOR, 'h1.title')
    filter_panel = (By.CSS_SELECTOR, "[data-role='filters-container']")
    filter_header_top = (By.CSS_SELECTOR, '.ui-collapse_list')
    filter_header_sub = (By.CSS_SELECTOR, ".ui-collapse_list .ui-collapse__link-text")
    close_list_icon = (By.CSS_SELECTOR, ".ui-collapse__icon_down")

    input_search = (By.CSS_SELECTOR, ".ui-input-search__input")
    range_search = (By.CSS_SELECTOR, ".ui-input-small__input")
    reset_button = (By.XPATH, "//button[@data-role='filters-reset']")
    apply_filter = (By.CSS_SELECTOR, "[data-role='filters-submit']")

    product_cart = (By.CSS_SELECTOR, "[data-id='product']")
    add_product_button = (By.CSS_SELECTOR, ".buy-btn")
    product_price = (By.CSS_SELECTOR, ".product-buy__price")
    content = (By.CSS_SELECTOR, ".products-list__content")

    # Getters
    def get_product(self, num):
        product = self.browser.find_elements(*self.product_cart)
        return product[num]

    # Actions
    def select_product(self, num):
        self.action.move_to_element(self.get_product(num)).perform()
        self.get_product(num).find_element(*self.add_product_button).click()
        time.sleep(2)
        print("Click product add-button")

    def read_product_price(self, num):
        price_element = self.get_product(num).find_element(*self.product_price)
        price = self.read_title(price_element)
        price = self.leave_numbers_2(price)
        return price

    # Methods
    def transition_to_menu_section_and_check(self, top_menu_text, second_menu_text):
        """open subsection and check load"""
        self.get_menu_section(top_menu_text, second_menu_text)
        self.check_open(self.section_name)
        self.assert_word(word=self.get_clickable_element(self.section_name), result=second_menu_text)

    def get_products_to_cart(self, num):
        """select and follow to cart"""
        for i in num:
            self.select_product(i)
        MainPage(self.browser).open_cart()
        assert self.get_current_url() == CartPage(self.browser).base_url
        assert self.get_len_elements(CartPage(self.browser).cart_item) == len(num)
    def select_filter(self, reset=True, **kwargs):
        print("Put Down Filters")
        if reset:
            reset_b = self.get_clickable_element(self.reset_button)
            self.action.move_to_element(reset_b).perform()
            reset_b.click()
            time.sleep(3)
            self.browser.execute_script("window.scrollTo(0, 700);")
        headers = self.browser.find_elements(*self.filter_header_sub)
        for key in kwargs.keys():
            header = self.browser.find_element(By.XPATH, f"//span[text()='{key}']")
            if header in headers:
                index = headers.index(header)  # определяем номер фильтра с которым будет работать по вхождению названия фильтра
                print(index)
                prod_filter = self.browser.find_elements(*self.filter_header_top)[index]  # находим сам фильтр
                self.action.move_to_element(prod_filter).perform()
                if self.is_composite_locator_present(prod_filter, self.close_list_icon[1]):  # проверяем фильтр на развернутость
                    prod_filter.click()
                    self.browser.execute_script("window.scrollBy(0, 200)")
                if type(kwargs.get(key)) == list:
                    lower_search = prod_filter.find_elements(*self.range_search)[0]
                    upper_search = prod_filter.find_elements(*self.range_search)[1]
                    lower_search.send_keys(kwargs.get(key)[0])
                    upper_search.send_keys(kwargs.get(key)[1])
                else:
                    self.browser.execute_script("window.scrollBy(0, 200)")
                    filter_search = prod_filter.find_element(*self.input_search)  # используем поиск фильтра
                    filter_search.send_keys(kwargs.get(key))
                    # checkbox = prod_filter.find_element(By.CSS_SELECTOR, "[data-id="brand"] .ui-checkbox:not([style="display: none;"])")
                    checkbox = self.browser.find_element(By.XPATH, f"//label/span[contains(text(), '{kwargs.get(key)}')]")
                    checkbox.click()
                    # self.browser.execute_script("arguments[0].click();", checkbox)
        apply_button = self.get_clickable_element(self.apply_filter)
        self.action.move_to_element(apply_button).perform()
        print("Apply Filters")
        apply_button.click()
        self.check_open(self.content)
        self.get_clickable_element(self.product_cart)
        self.action.move_to_element(self.get_product(0)).perform()

