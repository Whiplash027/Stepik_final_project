from .pages.product_page import ProductPage
from .pages.busket_page import BusketPage
from .pages.base_page import BasePage
from .pages.locators import ProductPageLocators
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link_busket = "http://selenium1py.pythonanywhere.com/basket/"
    page = ProductPage(browser, link)
    page.open()
    page.should_in_busket_add()
    page.solve_quiz_and_get_code()
    time.sleep(2)
    busket_page = BusketPage(browser, link_busket)
    time.sleep(2)
    busket_page.open()
    busket_page.complete_busket_checker
