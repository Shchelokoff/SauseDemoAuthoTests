from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.baseClass import Base

class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    checkoutButton = "//button[@id='checkout']"

    # Getters
    def getCheckoutButton(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkoutButton)))

    # Actions
    def clickCheckoutButton(self):
        self.getCheckoutButton().click()
        print("Click checkout button")

    # Methods
    def productConfirmation (self):
        self.getCurrentURL()
        self.clickCheckoutButton()




