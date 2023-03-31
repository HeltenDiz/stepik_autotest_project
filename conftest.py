import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


# @pytest.fisture()
# def set_up():
#     print("Start test")
#     options = Options()
#     options.add_experimental_option('excludeSwitches', ['enable-logging'])  # для чистки логов от лишнего
#     options.add_experimental_option("detach", True)  # чтоб не закрывалась страница хром
#     g = Service('C:\\Users\\da.boyarincev\\Downloads\\PyProjects\\resource\\chromedriver.exe')
#     driver = webdriver.Chrome(options=options, service=g)
#     base_url = 'https://www.saucedemo.com/'
#     driver.get(base_url)
#     driver.maximize_window()
#
#     yield
#
#     driver.quit()
#     print("Finish test")

@pytest.fixture()
def set_up():
    print("Start test")
    yield
    print("Finish test")


@pytest.fixture(scope="module")
def set_group():
    print("Enter system")
    yield
    print("Exit system")

