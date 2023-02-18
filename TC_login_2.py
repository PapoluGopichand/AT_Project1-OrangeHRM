# Orange CRM login Negative Scenario

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time


class HRM:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    username = "Admin"
    password = "admin124"
    username_locator = "username"
    password_locator = "password"
    loginButtonLocator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    login_information = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p'


    def login(self):
        self.browsing()
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=self.username_locator).send_keys(self.username)
        self.driver.find_element(by=By.NAME, value=self.password_locator).send_keys(self.password)
        self.driver.find_element(by=By.XPATH, value=self.loginButtonLocator).click()


    def browsing(self):
        self.driver.maximize_window()
        self.driver.get(self.url)

    def check_cookie(self):
        time.sleep(4)
        cookie_before = self.driver.get_cookies()[0]['value']
        cookie_after = self.driver.get_cookies()[0]['value']
        if cookie_before != cookie_after:
            print("LOGIN was success !")
        else:
            print("Invalid credentials")
        time.sleep(2)
        self.driver.quit()


H= HRM()

H.login()

H.check_cookie()
