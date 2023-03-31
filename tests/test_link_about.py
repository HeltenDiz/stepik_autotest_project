from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from stepik_autotest_project.pages.login_page import LoginPage
from stepik_autotest_project.pages.main_page import MainPage


class Test1:
    login_name = "standard_user"
    login_password = "secret_sauce"

    @classmethod
    def setUpClass(cls):
        """"""
        pass

    def test_link_about(self):
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

        mp = MainPage(driver)
        mp.select_product()

