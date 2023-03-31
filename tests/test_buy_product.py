import pytest
# from atf.pytest_core.base.case_ui import TestCaseUI
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from stepik_autotest_project_2.pages import CartPage
from stepik_autotest_project.pages.login_page import LoginPage


class Test1:  # TestCaseUI
    login_name = "standard_user"
    login_password = "secret_sauce"

    # @classmethod
    # def setUpClass(cls):
    #     """"""
    #     pass

    @pytest.mark.parametrize("num", (
            0, #1
    ))
    def test_buy_product(self, set_up, num):
        options = Options()
        options.add_experimental_option('excludeSwitches', ['enable-logging']) #для чистки логов от лишнего
        options.add_experimental_option("detach", True) #чтоб не закрывалась страница хром
        g = Service('C:\\Users\\da.boyarincev\\Downloads\\PyProjects\\resource\\chromedriver.exe')
        driver = webdriver.Chrome(options=options, service=g)

        print("Start Test")

        login = LoginPage(driver)
        login.authorization(self.login_name, self.login_password)

        # burger_menu = WebDriverWait(driver, 10).until(
        #             EC.element_to_be_clickable((By.XPATH, "//button[@id='react-burger-menu-btn']")))  # инонка меню
        # burger_menu.is_displayed()
        # burger_menu.click()
        # time.sleep(3)

        # mp = MainPage(driver)
        # mp.open_cart()
        # driver.quit()
        cp = CartPage(driver)
        cp.click_checkout()
        #
        # cip = ClientInfoPage(driver)
        # cip.input_information()
        #
        # pp = PaymentPage(driver)
        # pp.payment()
        #
        # f = FinishPage(driver)
        # f.check_finish()

    # if __name__ == '__main__':
    #     pytest.main()
