from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def should_in_busket_add(self):
        print(self.browser.find_element(*ProductPageLocators.GOOD_NAME).text)
        print(self.browser.find_element(*ProductPageLocators.GOOD_PRICE).text)
        self.browser.find_element(*ProductPageLocators.BUSKET_ADD_BTN).click()
     


