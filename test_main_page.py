
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.cart_page import CartPage
def test_guest_can_go_to_login_page(browser):
     link = "http://selenium1py.pythonanywhere.com/"
     page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
     page.open()                      # открываем страницу
     page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    # pytest -v --tb=line --language=en test_main_page.py
    # --tb=line, которая указывает, что нужно выводить только одну строку из лога каждого упавшего теста
     login_page = LoginPage(browser, browser.current_url)
     login_page.should_be_login_page()
def test_guest_should_be_login_form(browser): # Язык не меняется!!!!
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()

def test_guest_should_be_login_url(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()

def test_guest_should_be_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    main_link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = MainPage(browser, main_link)
    page.open()
    page.go_to_basket_page()
    page = CartPage(browser, browser.current_url)
    page.open()
    page.should_not_be_products_in_the_basket()
    page.should_not_be_products_in_the_basket_msg()
