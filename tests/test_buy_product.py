import pytest

from pages.cart_page import CartPage
from pages.client_info_page import ClientCheckoutPage
from pages.login_page import LoginPage
from pages.product_selection_page import ProductSelectionPage


@pytest.mark.usefixtures("browser")
class TestBuyProduct:
    login_name = "Zuldim@yandex.ru"
    login_password = "dxvc23847b"
    top_menu = ProductSelectionPage.computer_parts
    submenu = ProductSelectionPage.video_card
    phone_num = "89787425279"
    mail_name = "game005@gmail.com"
    method_name = "Самовывоз"
    pay_method_name = "При получении"

    @pytest.fixture(scope="class")
    def setup_class(self):
        LoginPage(self.browser).authorization(user_name=self.login_name, user_password=self.login_password)

    @pytest.fixture(scope="function")
    def set_up(self):
        print("Start function")
        ProductSelectionPage(self.browser).open_main_page()
        ProductSelectionPage(self.browser).transition_to_menu_section_and_check(self.top_menu, self.submenu)
        yield
        print("Finished Test")

    @pytest.mark.parametrize("kwargs", (
            ({'num_1': 0, 'num_2': 1,
              'filter_dict': {'Производитель': 'GIGABYTE', 'Графический процессор': 'GeForce RTX 3060 Ti',
                              'Цена': ['3000', '70000']}}),
            ({'num_1': 1, 'num_2': 2,
              'filter_dict': {'Производитель': 'MSI', 'Графический процессор': 'GeForce RTX 4070 Ti',
                              'Цена': ['86000', '100000']}})
    ))
    def test_1_product_choice(self, set_up, setup_class, kwargs):
        product_p = ProductSelectionPage(self.browser)
        cart_p = CartPage(self.browser)
        checkout = ClientCheckoutPage(self.browser)
        print("Clean cart and filters")
        product_p.clean_cart()
        product_p.select_filter(**kwargs['filter_dict'])

        print("Choose products and compare prices with the basket")
        price_1 = product_p.read_product_price(num=kwargs['num_1'])
        price_2 = product_p.read_product_price(num=kwargs['num_2'])

        product_p.get_products_to_cart(num=(kwargs['num_1'], kwargs['num_2']))

        cart_price_1 = cart_p.read_price(cart_p.product_price, num=kwargs['num_1'])
        cart_price_2 = cart_p.read_price(cart_p.product_price, num=kwargs['num_2'])

        assert price_1 == cart_price_1, "price does not match"
        assert price_2 == cart_price_2, "price does not match"

        sum_price = int(cart_price_1) + int(cart_price_2)
        final_price = cart_p.read_price(cart_p.final_price, num=0)
        print("Сompare final prices")
        assert int(sum_price) == int(final_price), "final price does not match"

        cart_p.click_to_order()
        checkout.fill_information_and_confirm(self.phone_num, self.mail_name, self.method_name, self.pay_method_name)
