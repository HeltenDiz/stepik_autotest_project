import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options as ch_options
from selenium.webdriver.firefox.options import Options as fr_options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='ru')


@pytest.fixture(scope="class")
def browser(request):
    user_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")

    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = ch_options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        options.add_experimental_option('excludeSwitches', ['enable-logging'])  # для чистки логов от лишнего
        options.add_experimental_option("detach", True)  # чтоб не закрывалась страница хром
        options.add_argument("--start-maximized")  # open Browser in maximized mode

        #  g = Service('C:\\Users\\da.boyarincev\\Downloads\\PyProjects\\resource\\chromedriver.exe')

        # options.add_argument('--headless')
        # options.add_argument('--no-sandbox')
        # options.add_argument('--disable-dev-shm-usage')

        browser = webdriver.Chrome(options=options)  #service=g
        browser.implicitly_wait(time_to_wait=10)
        # base_url = 'https://www.saucedemo.com/'
        # browser.get(base_url)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options = fr_options()
        profile = webdriver.FirefoxProfile()
        profile.set_preference('intl.accept_languages', user_language)
        browser = webdriver.Firefox(options=options, firefox_profile=profile)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    request.cls.browser = browser  # объявляем переменную класса - browser, для использования с @pytest.mark.usefixtures("browser")
    yield browser  # на случай использования browser для scope=function
    time.sleep(2)
    print("\nquit browser..")
    browser.quit()



# @pytest.fixture(scope="class")
# def setup_class():
#     print("Start tests")
#     yield browser
#     print("Finish tests")
#
#
# @pytest.fixture(scope="function")
# def setUp():
#     print("Start function")
#     yield
#     print("Exit function")

