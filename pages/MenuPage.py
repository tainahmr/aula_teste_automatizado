from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.PageObject import PageObject


class MenuPage(PageObject):
    menu_icon = (By.ID, 'react-burger-menu-btn')
    menu_close_icon = (By.ID, 'react-burger-cross-btn')
    logout_menu_item = (By.ID, 'logout_sidebar_link')

    def __init__(self, driver):
        super(MenuPage, self).__init__(driver=driver)

    def open_menu(self):
        self.driver.find_element(*self.menu_icon).click()

    def is_menu_opened(self):
        menu_element = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.menu_close_icon))
        return menu_element.is_displayed()

    def click_logout(self):
        self.driver.find_element(*self.logout_menu_item).click()

    def open_cart(self):
        raise Exception('NThis function is not supported!')