from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    
    def add_product_to_basket(self):
        find_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name = find_product_name.text
        
        find_product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price = find_product_price.text
        
        add_to_busket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BUSKET_BTN)
        add_to_busket_btn.click()

        self.solve_quiz_and_get_code()

        find_product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE)
        product_name_in_message = find_product_name_in_message.text

        find_product_price_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE)
        product_price_in_message = find_product_price_in_message.text
        print(f"{product_name_in_message = }\n{product_price_in_message = }")

        assert product_name in product_name_in_message, "Names are different"

        assert product_price in product_price_in_message, "Prices are different"


