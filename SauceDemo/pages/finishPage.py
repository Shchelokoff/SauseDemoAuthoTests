from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.baseClass import Base

class FinishPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    selectProduct1 = "//button[@id='add-to-cart-sauce-labs-backpack']"
    cart = "//div[@id='shopping_cart_container']"

    # Getters

    # Actions

    # Methods
    def finish(self):
        self.getCurrentURL()
        self.assertURL('https://www.saucedemo.com/checkout-complete.html')
        self.getScreenshot()





