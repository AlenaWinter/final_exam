from .base_page import BasePage #импорт базового класса BasePage
from selenium.webdriver.common.by import By
from .login_page import LoginPage
from .locators import MainPageLocators #импортируем MainPageLocators из файла locators.py
class MainPage(BasePage): # класс  MainPage: Его нужно сделать наследником класса BasePage. Класс-предок в Python указывается в скобках
    def go_to_login_page(self):    # Создание метода, позволяющего попасть на страницу авторитизации
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url) #проинициализировать новый объект Page и вернуть его
        alert = self.browser.switch_to.alert
        alert.accept()
    def should_be_login_link(self):
         assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented" # осмысленное сообщение об ошибке
    