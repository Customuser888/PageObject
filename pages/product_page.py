from .locators import ProductPageLocators
from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException # в начале файла
import time
import math

class ProductPage(BasePage):
    def product_page(self):
        #self.should_be_newYear_url()
        
        enter1 = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_BUTTON)
        enter1.click()
        
        self.solve_quiz_and_get_code()
        time.sleep(3)
        self.return_book_name()
        self.return_book_price()
        
        self.product_name_matches_the_one_added(self.return_book_name())
        self.price_is_the_same_as_product(self.return_book_price())
        
        
    def should_be_newYear_url(self):
        assert '?promo=newYear' in self.browser.current_url, 'newYear missing'
    
    def return_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return book_name.text

    def return_book_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        return book_price.text

    def product_name_matches_the_one_added(self, book_name):
        alert_book_name = self.browser.find_element(*ProductPageLocators.ALERT_BOOK_NAME)
        assert book_name == alert_book_name.text, f"book name is {book_name}, but alert book name is {alert_book_name}"
    def price_is_the_same_as_product(self, book_price):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        assert basket_price.text == book_price, f"basket prise is {basket_price}, but book price is {book_price}"

    
