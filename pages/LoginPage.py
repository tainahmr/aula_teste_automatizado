from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class LoginPage(PageObject):
    url = 'https://www.saucedemo.com/'
    login_btn = (By.ID, 'login-button')
    error_message_login = (By.CSS_SELECTOR, '[data-test="error"]')
    error_text_message = 'Epic sadface: Username is required'
    username_field = (By.CSS_SELECTOR, '[placeholder="Username"]')
    password_field = (By.ID, 'password')

    def __init__(self, browser):
        super(LoginPage, self).__init__(browser=browser)

    def open_login_page(self):
        self.driver.get(self.url)

    def click_login_button(self):
        self.driver.find_element(*self.login_btn).click()

    def is_url_login(self):
        return self.is_url(self.url)

    def has_message_login_message_error(self):
        error_message_element = self.driver.find_element(*self.error_message_login)
        is_message_displayed = error_message_element.is_displayed()
        has_message_text = error_message_element.text == self.error_text_message
        return is_message_displayed and has_message_text

    def execute_login(self, username='standard_user', password='secret_sauce'):
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.click_login_button()

    def open_cart(self):
        raise Exception('NThis function is not supported!')
