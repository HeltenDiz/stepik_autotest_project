from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class MainPage(Base):
    base_url = 'https://www.dns-shop.ru'

    # Locators of current class
    home_page = (By.CSS_SELECTOR, ".homepage__top-grid")
    top_panel_catalog = (By.XPATH, "//span[@data-role='catalog-button']")
    submenu = (By.CSS_SELECTOR, ".catalog-submenu .ui-link.header-catalog-submenu-item")
    menu_section = (By.XPATH, "//a[@class='catalog-menu__link-wrapper']")
    second_menu_section = (By.XPATH, "//a[@class='ui-link header-catalog-submenu-item']")
    cart_button = (By.XPATH, "//a[@data-commerce-target='CART']")
    items_in_cart = (By.XPATH, "//span[@class='cart-link-counter__badge']")
    remove_items = (By.XPATH, "//span[@class='cart-group__header-remove-btn']")

    # menu_section_name
    computers = 'Бытовая техника'
    org_technique = 'Смартфоны и фототехника'
    computer_parts = 'Комплектующие для ПК'

    # subsection name
    video_card = 'Видеокарты'

    # Actions
    def open_cart(self):
        self.get_clickable_element(self.cart_button).click()
        print("Open cart")

    def open_cart_menu(self):
        cart_btn = self.get_clickable_element(self.cart_button)
        self.action.move_to_element(cart_btn).perform()

    def get_menu_section(self, top_menu_text, second_menu_text):
        """open menu and choose subsection"""
        self.get_clickable_element(self.top_panel_catalog).click()
        self.check_open(self.submenu)
        first_menu_section = self.get_clickable_element(self.menu_section).find_element(By.XPATH, f"//a[text()='{top_menu_text}']")
        self.action.move_to_element(first_menu_section).perform()
        self.check_open(self.submenu)
        submenu_section = self.get_clickable_element((By.XPATH, f"{self.second_menu_section[1]} //span[text()='{second_menu_text}']"))
        submenu_section.click()
        print("Open submenu")

    # Methods

    def clean_cart(self):
        if self.is_element_present(self.items_in_cart):
            self.open_cart_menu()
            self.get_clickable_element(self.remove_items).click()

    def open_main_page(self):
        self.browser.get(self.base_url)
        self.check_open(self.home_page)



    # def select_menu_chapter_2(self, name_chapter, correct_url):
    #     list_elements_text = [elements.text for elements in self.dropdown]
    #     for element in list_elements_text:
    #         if element[0] == name_chapter:
    #             self.chapters.find_element(By.NAME, name_chapter).click()
    #             break
    #         if element[1] == name_chapter:
    #             self.chapters.find_element(By.NAME, name_chapter).click()
    #             break
    #         if element[2] == name_chapter:
    #             self.chapters.find_element(By.NAME, name_chapter).click()
    #             break
    #         if element[3] == name_chapter:
    #             self.chapters.find_element(By.NAME, name_chapter).click()
    #             break
    #     self.assert_url(correct_url)
    #
    # def select_menu_chapter_3(self, correct_url, **kwargs):
    #     if kwargs.get('All Items'):
    #         self.chapters.find_element(By.NAME, kwargs).click()
    #     if kwargs.get('About'):
    #         self.chapters.find_element(By.NAME, kwargs).click()
    #     if kwargs.get('Logout'):
    #         self.chapters.find_element(By.NAME, kwargs).click()
    #     if kwargs.get('Reset App State'):
    #         self.chapters.find_element(By.NAME, kwargs).click()
    #     self.assert_url(correct_url)
