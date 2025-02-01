from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    
    '''
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")
    
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON = (By.NAME, "login_submit")
    '''

class ProductPageLocators():
    ADD_PRODUCT_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ITEM_ADDED_TO_CART = (By.CSS_SELECTOR, ".alertinner strong")
    #ITEM_ADDED_TO_CART = (By.CSS_SELECTOR, '.alert-safe:nth-of-type(1) .alertinner strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.product_main h1')
    BASKET_VALUE = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
    COST_OF_GOOD = (By.CSS_SELECTOR, 'p.price_color')