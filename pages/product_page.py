from .locators import ProductPageLocators    # Импорт класса, описывающего главную страницу
from .base_page import BasePage            # Импорт базового класса BasePage


class ProductPage(BasePage):
    def add_product_to_cart(self):
        link = self.browser.find_element(*ProductPageLocators.BASKET_BTN)
        link.click()
        self.solve_quiz_and_get_code()
