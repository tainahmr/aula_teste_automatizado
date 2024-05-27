import pytest
from selenium.webdriver.common.by import By

from pages.LoginPage import LoginPage
from pages.ProductsPage import ProductsPage

url = 'https://www.saucedemo.com/'
url_products = 'https://www.saucedemo.com/inventory.html'


def pytest_addoption(parser):
    parser.addoption("--browser_selenium", default='chrome', help='Select browser')

@pytest.fixture()
def run_all_browser(all_browsers):
    login_page = LoginPage(browser=all_browsers)
    login_page.open_login_page()
    yield login_page
    # Pos condicao
    login_page.close()


@pytest.fixture()
def browser_selected(request):
    selected_browser = request.config.getoption('--browser_selenium').lower()
    yield selected_browser


@pytest.fixture()
def setup(browser_selected):
    # Pre condicao: abrir o browser e acessar a página.
    login_page = LoginPage(browser=browser_selected)
    login_page.open_login_page()
    yield login_page
    # Pos condicao
    login_page.close()


@pytest.fixture
def login_app(setup):
    login_page = setup
    login_page.execute_login()
    products_page = ProductsPage(driver=login_page.driver)
    assert products_page.is_url_products(), 'URL de produtos não encontrada!'
    yield login_page, products_page