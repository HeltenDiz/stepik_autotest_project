from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class MainPage(Base):
    base_url = 'https://www.computeruniverse.net/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_driver(self):
        return self.driver

    # Locators
    ""
    login_popup = (By.CLASS_NAME, "[class='c-LoginPopOver__content']")
    username = (By.ID, "[id='login-form_id']")
    password = (By.ID, "[id='login-form_password']")
    button_login = (By.LINK_TEXT, "button.at__login__login")

    top_panel_menu = (By.CSS_SELECTOR, ".TopMenuPanel_panel__body__HqNJ_")
    cart_button = (By.TAG_NAME, "button.at__header_cart")

    #link_text lvl 1
    computers = 'Ноутбуки/ ПК/ планшеты'
    org_technique = 'Оргтехника и периферия'

    add_product_button = '.inventory_item_description .btn_inventory'
    # product_description = get_driver().find_elements(By.CSS_SELECTOR, ".inventory_item_description")
    # inventory_image = get_driver().find_element(By.CSS_SELECTOR, ".inventory_item_img")  # картинка товара
    # add_to_cart = get_driver().find_elements(By.CSS_SELECTOR,
    #                                          '.inventory_item_description .btn_inventory')  # кнопка добавить в корзину
    #
    # product_title = get_driver().find_element(By.CSS_SELECTOR, ".inventory_item_name")
    # burger_menu = "//button[@id='react-burger-menu-btn']"
    # chapters = get_driver().find_elements(By.CSS_SELECTOR, ".bm-item.menu-item")
    # dropdown = get_driver().find_element(By.CSS_SELECTOR, ".bm-item-list")

    # Getters

    def get_top_menu_panel(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.top_panel_menu))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.cart_button))

    # Actions
    def select_product(self, num):
        self.get_add_product_button().is_displayed()
        self.add_to_cart[num].click()
        print("Click product add-button")

    def open_cart(self):
        self.get_cart_button().click()
        print("Open cart")

    def click_burger_menu(self):
        self.get_burger_menu().click()
        print("Open menu")

    # Methods

    def select_and_buy_product(self, num):
        """select and follow to cart"""
        self.get_current_url()
        self.select_product(num)
        self.open_cart()

    def select_menu_chapter(self, name_chapter, correct_url):
        """open menu and choose chapter"""
        self.click_burger_menu()
        chapter = self.chapters.find_element(By.NAME, name_chapter)
        chapter.click()
        self.assert_url(correct_url)

    def select_menu_chapter_2(self, name_chapter, correct_url):
        list_elements_text = [elements.text for elements in self.dropdown]
        for element in list_elements_text:
            if element[0] == name_chapter:
                self.chapters.find_element(By.NAME, name_chapter).click()
                break
            if element[1] == name_chapter:
                self.chapters.find_element(By.NAME, name_chapter).click()
                break
            if element[2] == name_chapter:
                self.chapters.find_element(By.NAME, name_chapter).click()
                break
            if element[3] == name_chapter:
                self.chapters.find_element(By.NAME, name_chapter).click()
                break
        self.assert_url(correct_url)

    def select_menu_chapter_3(self, correct_url, **kwargs):
        if kwargs.get('All Items'):
            self.chapters.find_element(By.NAME, kwargs).click()
        if kwargs.get('About'):
            self.chapters.find_element(By.NAME, kwargs).click()
        if kwargs.get('Logout'):
            self.chapters.find_element(By.NAME, kwargs).click()
        if kwargs.get('Reset App State'):
            self.chapters.find_element(By.NAME, kwargs).click()
        self.assert_url(correct_url)