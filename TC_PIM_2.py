# Edit an exiting employee in the PIM module

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time
from selenium.webdriver.common.action_chains import ActionChains


class HRM:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    username = "Admin"
    password = "admin123"
    username_locator = "username"
    password_locator = "password"
    loginButtonLocator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    pim_locator = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'
    editButton_locator= '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[2]/i'
    First_Name = "Ram"
    Middle_Name = "Krishna"
    Last_Name = "R"
    first_name_locator = "firstName"
    middle_name_locator = "middleName"
    last_name_locator = "lastName"
    saveButton_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button'

    def login(self):
        self.browsing()
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=self.username_locator).send_keys(self.username)
        self.driver.find_element(by=By.NAME, value=self.password_locator).send_keys(self.password)
        self.driver.find_element(by=By.XPATH, value=self.loginButtonLocator).click()
    def PIM(self):
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=self.pim_locator).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=self.editButton_locator).click()

    def edit(self):
        time.sleep(5)
        first_name_locator=self.driver.find_element(by=By.NAME, value=self.first_name_locator)
        middle_name_locator=self.driver.find_element(by=By.NAME, value=self.middle_name_locator)
        last_name_locator=self.driver.find_element(by=By.NAME, value=self.last_name_locator)

        action= ActionChains(self.driver)
        action.double_click(on_element=first_name_locator).double_click().send_keys(self.First_Name).perform()
        action.double_click(on_element=middle_name_locator).double_click().send_keys(self.Middle_Name).perform()
        action.double_click(on_element=last_name_locator).double_click().send_keys(self.Last_Name).perform()
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        saveButton_locator = self.driver.find_element(by=By.XPATH, value=self.saveButton_locator)
        action.move_to_element(saveButton_locator).click().perform()

        time.sleep(5)
        self.driver.quit()

    def browsing(self):
        self.driver.maximize_window()
        self.driver.get(self.url)


H=HRM()
H.login()

H.PIM()
H.edit()
print("Edited employee information successfully")