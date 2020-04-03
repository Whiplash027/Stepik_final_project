from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
class ProductPageLocators():
    BUSKET_ADD_BTN = (By.CSS_SELECTOR , "#add_to_basket_form > button")
    BUSKET_WATCH_BTN = (By.XPATH , '//*[@id="default"]/header/div[1]/div/div[2]/span/a')
    GOOD_NAME = (By.XPATH , '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    GOOD_PRICE = (By.XPATH , '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
