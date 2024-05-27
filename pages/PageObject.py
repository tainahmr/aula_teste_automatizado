from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By


class PageObject:

    cart_icon = (By.CLASS_NAME, 'shopping_cart_link')

    def __init__(self, driver=None, browser=None):
        if driver:
            self.driver = driver
        else:
            # Criar webdriver (browser)
            if browser == 'chrome':
                self.driver = webdriver.Chrome()
            elif browser == 'firefox':
                self.driver = webdriver.Firefox()
            elif browser == 'safari':
                self.driver = webdriver.Safari()
            else:
                raise Exception('Browser não suportado!!!')

    def is_url(self, url):
        return self.driver.current_url == url

    def open_cart(self):
        self.driver.find_element(*self.cart_icon).click()

    def close(self):
        self.driver.quit()