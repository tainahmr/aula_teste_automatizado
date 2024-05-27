import pytest

from pages.MenuPage import MenuPage


class Test3:

    def test_logout_app(self, login_app):
        login_page, products_page = login_app
        # Abrir o menu
        menu_page = MenuPage(driver=products_page.driver)
        menu_page.open_menu()
        assert menu_page.is_menu_opened(), 'Menu não foi aberto!'
        # Clicar no botão Logout.
        menu_page.click_logout()
        assert login_page.is_url_login(), "Página login não encontrada!"