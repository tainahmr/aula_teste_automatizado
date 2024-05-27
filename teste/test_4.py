from pages.CartPage import CartPage


class Test4:

    def test_add_product_to_cart(self, login_app):
        login_page, products_page = login_app
        product_name = products_page.add_product_to_cart()
        assert products_page.get_products_in_cart() == 1, 'Número no carrinho de compras incorreto!'

        products_page.open_cart()
        cart_page = CartPage(driver=products_page.driver)
        assert cart_page.is_url_cart_page(), 'Cart page url not found1'
        assert cart_page.has_title(), 'Cart page title not found'

        assert cart_page.get_first_product_name_in_cart_list() == product_name, 'Nome do produto incorreto!'


