from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.baseClass import Base

class PaymentPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    finishButton = "//button[@id='finish']"


    # Getters
    def getFinishButton(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.finishButton)))

    # Actions
    def clickfinishButton(self):
        self.getFinishButton().click()
        print("Click finish button")

    # Methods
    def payment(self):
        self.getCurrentURL()
        self.clickfinishButton()




