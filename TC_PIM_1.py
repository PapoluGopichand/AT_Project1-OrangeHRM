# Adding a new employee in the PIM

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
    add_emp_locator = '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]'
    First_Name = "Gopi"
    Middle_Name= "Chand"
    Last_Name= "Papolu"
    first_Name_locator= "firstName"
    middle_Name_locator="middleName"
    last_Name_locator="lastName"
    save_button_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'


    def login(self):
        self.browsing()
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=self.username_locator).send_keys(self.username)
        self.driver.find_element(by=By.NAME, value=self.password_locator).send_keys(self.password)
        self.driver.find_element(by=By.XPATH, value=self.loginButtonLocator).click()
    def PIM(self):
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=self.pim_locator).click()
    def Click_add_employee(self):
         time.sleep(5)
         add_emp_locator= self.driver.find_element(by=By.XPATH, value=self.add_emp_locator)
         action=ActionChains(self.driver)
         action.click(on_element=add_emp_locator).perform()

    def Add_Employee_data(self):
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=self.first_Name_locator).send_keys(self.First_Name)
        self.driver.find_element(by=By.NAME, value=self.middle_Name_locator).send_keys(self.Middle_Name)
        self.driver.find_element(by=By.NAME, value=self.last_Name_locator).send_keys(self.Last_Name)
        save_button_locator = self.driver.find_element(by=By.XPATH, value=self.save_button_locator)
        action = ActionChains(self.driver)
        action.click(on_element=save_button_locator).perform()
        time.sleep(5)
        self.driver.quit()

    def browsing(self):
        self.driver.maximize_window()
        self.driver.get(self.url)

H= HRM()

H.login()
H.PIM()

H.Click_add_employee()
H.Add_Employee_data()

print("New employee added successfully")
