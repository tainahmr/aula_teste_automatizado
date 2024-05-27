import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.PageObject import PageObject


class ProductsPage(PageObject):
    url = 'https://www.saucedemo.com/inventory.html'
    title_products = (By.CSS_SELECTOR, '.title')
    products_text_title = 'Products'
    shopping_cart_badge = (By.CLASS_NAME, 'shopping_cart_badge')
    remove_text_btn = 'Remove'
    add_to_cart_text_btn = 'Add to cart'
    remove_btn = (By.CLASS_NAME, 'btn_secondary')
    add_to_cart_btn = (By.CLASS_NAME, 'btn_primary')
    products_list_elements = (By.CLASS_NAME, 'inventory_item')
    product_name_in_card = (By.CLASS_NAME, 'inventory_item_name')
    product_filter = (By.CLASS_NAME, 'product_sort_container')
    product_price = (By.CLASS_NAME, 'inventory_item_price')

    def __init__(self, driver):
        super(ProductsPage, self).__init__(driver=driver)

    def is_url_products(self):
        return self.is_url(self.url)

    def has_products_title(self):
        products_title = self.driver.find_element(*self.title_products)
        return products_title.is_displayed() and products_title.text == self.products_text_title

    def add_product_to_cart(self):
        products_list = self.driver.find_elements(*self.products_list_elements)
        random_index = random.randint(0, len(products_list) - 1)
        product_card = products_list[random_index]
        add_to_cart_btn = product_card.find_element(*self.add_to_cart_btn)
        if add_to_cart_btn.text != self.add_to_cart_text_btn:
            raise Exception('Nome do botão Add to Cart incorreto!')
        add_to_cart_btn.click()
        remove_btn = product_card.find_element(*self.remove_btn)
        if remove_btn.text != self.remove_text_btn:
            raise Exception('Nome do botão Remove incorreto!')
        return product_card.find_element(*self.product_name_in_card).text

    def get_products_in_cart(self):
        return int(self.driver.find_element(*self.shopping_cart_badge).text)

    def filter_products_low_to_high(self):
        product_filter_element = self.driver.find_element(*self.product_filter)
        Select(product_filter_element).select_by_visible_text('Price (low to high)')

    def check_order_price_low_to_high(self):
        all_price_items = self.driver.find_elements(*self.product_price)
        result = False

        for i in range(len(all_price_items) -1):
            current_price = float(all_price_items[i].text.replace('$', ''))
            next_price = float(all_price_items[i + 1].text.replace('$', ''))

            if current_price > next_price:
                return False
        return True
