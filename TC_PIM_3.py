# Deleting an existing employee in the PIM module

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time


class HRM:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    username = "Admin"
    password = "admin123"
    username_locator = "username"
    password_locator = "password"
    loginButtonLocator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    pim_locator = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'
    deleteButton_locator= '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[1]/i'
    deleteAccept_locator= '/html/body/div/div[3]/div/div/div/div[3]/button[2]'

    def login(self):
        self.browsing()
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=self.username_locator).send_keys(self.username)
        self.driver.find_element(by=By.NAME, value=self.password_locator).send_keys(self.password)
        self.driver.find_element(by=By.XPATH, value=self.loginButtonLocator).click()
    def PIM(self):
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=self.pim_locator).click()

    def Delete(self):
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=self.deleteButton_locator).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=self.deleteAccept_locator).click()

        time.sleep(5)
        self.driver.quit()

    def browsing(self):
        self.driver.maximize_window()
        self.driver.get(self.url)


H=HRM()
H.login()

H.PIM()
H.Delete()
print("Successfully deleted employee information")