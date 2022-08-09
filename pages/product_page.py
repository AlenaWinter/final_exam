from .locators import ProductPageLocators    # Импорт класса, описывающего главную страницу
from .base_page import BasePage            # Импорт базового класса BasePage


class ProductPage(BasePage):
    def add_product_to_cart(self):
        basket_btn = self.browser.find_element(*ProductPageLocators.BASKET_BTN)
        basket_btn.click()
        self.solve_quiz_and_get_code()

    def get_msg_success(self):
        msg_product = self.browser.find_element(*ProductPageLocators.MSG_PRODUCT).text
        product_name = self.get_product_name()
        product_name_len = len(product_name)
        msg_success = msg_product[(product_name_len+1):]
        print(msg_success)
        return msg_success

    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        # print(product_name)
        return product_name

    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        print(product_price)
        return product_price

    def get_msg_product(self):
        msg_product = self.browser.find_element(*ProductPageLocators.MSG_PRODUCT).text
        print(msg_product)
        return msg_product