from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.baseClass import Base

class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    selectProduct1 = "//button[@id='add-to-cart-sauce-labs-backpack']"
    selectProduct2 = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    selectProduct3 = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    cart = "//div[@id='shopping_cart_container']"
    menu = "//button[@id='react-burger-menu-btn']"
    linkAbout = "//a[@id='about-sidebar-link']"

    # Getters
    def getSelectProduct1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.selectProduct1)))
    def getSelectProduct2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.selectProduct2)))
    def getSelectProduct3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.selectProduct3)))
    def getCart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))
    def getMenu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu)))
    def getLinkAbout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.linkAbout)))

    # Actions
    def clickSelectProducts1(self):
        self.getSelectProduct1().click()
        print("Select product1")
    def clickSelectProducts2(self):
        self.getSelectProduct2().click()
        print("Select product2")
    def clickSelectProducts3(self):
        self.getSelectProduct3().click()
        print("Select product3")
    def clickCart(self):
        self.getCart().click()
        print("Click cart")
    def clickMenu(self):
        self.getMenu().click()
        print("Click menu")
    def clickLinkAbout(self):
        self.getLinkAbout().click()
        print("Click link about")

    # Methods
    def PushInCartProduct1(self):
        self.getCurrentURL()
        self.clickSelectProducts1()
        self.clickCart()
    def PushInCartProduct2(self):
        self.getCurrentURL()
        self.clickSelectProducts2()
        self.clickCart()
    def PushInCartProduct3(self):
        self.getCurrentURL()
        self.clickSelectProducts3()
        self.clickCart()
    def selectMenuAbout(self):
        self.getCurrentURL()
        self.clickMenu()
        self.clickLinkAbout()
        self.assertURL('https://saucelabs.com/')
    def finish(self):
        self.getCurrentURL()
        self.assertURL('https://www.saucedemo.com/checkout-complete.html')
        self.getScreenshot()




