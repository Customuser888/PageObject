from .pages.main_page import MainPage
from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
import pytest


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"



@pytest.mark.parametrize('link', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, link):
    
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    print(f"TEST === # {link}")
    page = ProductPage(browser, link)
    page.open()
    product_page = page.product_page()
