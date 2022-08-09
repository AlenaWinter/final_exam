from .pages.product_page import ProductPage


class TestAddProductToBasket:
    def test_guest_can_add_product_to_cart(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_cart()
        # pytest -s test_product_page.py