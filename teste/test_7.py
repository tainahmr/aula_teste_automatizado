class Test7:

    def test_filter_product_low_to_high(self, login_app):
        login_page, products_page = login_app
        products_page.filter_products_low_to_high()
        assert products_page.check_order_price_low_to_high(), 'Ordem de preço dos produtos está incorreta!'
