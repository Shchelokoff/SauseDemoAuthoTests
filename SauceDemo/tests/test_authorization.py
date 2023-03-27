import time
import allure

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.loginPage import LoginPage
from pages.mainPage import MainPage

@allure.description("test_authorization")
def test_authorization():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='C:\\Users\\shche\\PycharmProjects\\resource\\chromedriver.exe', chrome_options=options)

    print('Chrome has started')

    login = LoginPage(driver)
    login.autorization()
    print('Finish test')
    m = MainPage(driver)
    m.getScreenshot()
    time.sleep(5)
    driver.quit()