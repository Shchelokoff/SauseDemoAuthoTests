import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.cartPage import CartPage
from pages.customerInfoPage import CustomerInfoPage
from pages.finishPage import FinishPage
from pages.loginPage import LoginPage
from pages.mainPage import MainPage
from pages.paymentPage import PaymentPage

@pytest.mark.run(order = 3)
def test_buy_product1():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='C:\\Users\\shche\\PycharmProjects\\resource\\chromedriver.exe', chrome_options=options)
    print('Chrome has started')
    login = LoginPage(driver)
    login.autorization()
    mp = MainPage(driver)
    mp.PushInCartProduct1()
    cp = CartPage(driver)
    cp.clickCheckoutButton()
    cip = CustomerInfoPage(driver)
    cip.inputCustomerInfo()
    p = PaymentPage(driver)
    p.clickfinishButton()
    f = FinishPage(driver)
    f.getScreenshot()
    print('Finish test 1')
    time.sleep(5)
    driver.quit()

@pytest.mark.run(order = 2)
def test_buy_product2():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='C:\\Users\\shche\\PycharmProjects\\resource\\chromedriver.exe', chrome_options=options)
    print('Chrome has started')
    login = LoginPage(driver)
    login.autorization()
    mp = MainPage(driver)
    mp.PushInCartProduct2()
    cp = CartPage(driver)
    cp.clickCheckoutButton()
    cip = CustomerInfoPage(driver)
    cip.inputCustomerInfo()
    p = PaymentPage(driver)
    p.clickfinishButton()
    f = FinishPage(driver)
    f.getScreenshot()
    print('Finish test 2')
    time.sleep(5)
    driver.quit()

@pytest.mark.run(order = 1)
def test_buy_product3():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='C:\\Users\\shche\\PycharmProjects\\resource\\chromedriver.exe', chrome_options=options)
    print('Chrome has started')
    login = LoginPage(driver)
    login.autorization()
    mp = MainPage(driver)
    mp.PushInCartProduct3()
    cp = CartPage(driver)
    cp.clickCheckoutButton()
    cip = CustomerInfoPage(driver)
    cip.inputCustomerInfo()
    p = PaymentPage(driver)
    p.clickfinishButton()
    f = FinishPage(driver)
    f.getScreenshot()
    print('Finish test 3')
    time.sleep(5)
    driver.quit()

