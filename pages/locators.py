from sre_constants import SUCCESS
from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BUSKET_BTN = (By.CSS_SELECTOR, "#add_to_basket_form .btn")

    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p")
    
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) strong")
    PRODUCT_PRICE_IN_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) strong")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:first-child")