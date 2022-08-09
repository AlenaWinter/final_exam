from selenium.webdriver.common.by import By

class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators(object):
    LOGIN_URL = (By.CSS_SELECTOR, "#id_login-redirect_url")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators(object):
     BASKET_BTN = (By.CSS_SELECTOR, "#add_to_basket_form > button")
     PRODUCT_NAME = (By.CSS_SELECTOR, "#content_inner h1")
     PRODUCT_PRICE = (By.CSS_SELECTOR, "#content_inner .price_color")

     MSG_PRODUCT = (By.CSS_SELECTOR, "#messages .alertinner")