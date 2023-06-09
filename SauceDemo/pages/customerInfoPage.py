from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.baseClass import Base

class CustomerInfoPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    firstName = "//input[@id='first-name']"
    lastName = "//input[@id='last-name']"
    postalCode = "//input[@id='postal-code']"
    continueButton = "//input[@id='continue']"

    # Getters
    def getFirstName(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.firstName)))
    def getLastName(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.lastName)))
    def getPostalCode(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.postalCode)))
    def getContinueButton(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continueButton)))

    # Actions
    def inputFirstName(self, firstName):
        self.getFirstName().send_keys(firstName)
        print("Input first name")
    def inputLastName(self, lastName):
        self.getLastName().send_keys(lastName)
        print("Input last name")
    def inputPostalCode(self, postalCode):
        self.getPostalCode().send_keys(postalCode)
        print("Input postal code")
    def clickContinueButton(self):
        self.getContinueButton().click()
        print("Click continue button")

    # Methods
    def inputCustomerInfo(self):
        self.getCurrentURL()
        self.inputFirstName("Дядя")
        self.inputLastName("Фёдор")
        self.inputPostalCode("Простоквашино")
        self.clickContinueButton()




