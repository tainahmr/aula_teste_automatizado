from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class CartPage(PageObject):

    url = 'https://www.saucedemo.com/cart.html'
    title_element = (By.CSS_SELECTOR, '.title')
    cart_title_text = 'Your Cart'
    cart_name_item = (By.CLASS_NAME, 'inventory_item_name')

    def __init__(self, driver):
        super(CartPage, self).__init__(driver=driver)

    def is_url_cart_page(self):
        return self.is_url(self.url)

    def has_title(self):
        return self.driver.find_element(*self.title_element).text == self.cart_title_text

    def get_first_product_name_in_cart_list(self):
        return self.driver.find_element(*self.cart_name_item).text
