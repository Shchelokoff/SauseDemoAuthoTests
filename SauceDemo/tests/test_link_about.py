import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.cartPage import CartPage
from pages.customerInfoPage import CustomerInfoPage
from pages.finishPage import FinishPage
from pages.loginPage import LoginPage
from pages.mainPage import MainPage
from pages.paymentPage import PaymentPage


def test_link_about():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='C:\\Users\\shche\\PycharmProjects\\resource\\chromedriver.exe', chrome_options=options)

    print('Chrome has started')

    login = LoginPage(driver)
    login.autorization()

    mp = MainPage(driver)
    mp.selectMenuAbout()

    f = FinishPage(driver)
    f.getScreenshot()

    print('Finish test')

    time.sleep(5)
    driver.quit()