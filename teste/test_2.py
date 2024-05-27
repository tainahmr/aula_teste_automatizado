import pytest

from pages.ProductsPage import ProductsPage


class Test2:

    def test_efetuar_login(self, setup):
        login_page = setup
        login_page.execute_login()

        products_page = ProductsPage(driver=login_page.driver)
        assert products_page.is_url_products(), 'URL de produtos não encontrada!'
        assert products_page.has_products_title(), 'Título Products não encontrado!'

