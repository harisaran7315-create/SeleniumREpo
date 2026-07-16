from selenium.webdriver.common.by import By

from BrowserUtils  import BrowserUtils
from ShopPage import Shop

class BrowserAutomation(BrowserUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username = (By.ID, "username")
        self.password = (By.ID, "password")
        self.SignButton = (By.ID, "signInBtn")

    def LoginUp(self, username, password):
        self.driver.get("https://rahulshettyacademy.com/loginpagePractise/")
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.SignButton).click()
        Shop_page = Shop(self.driver)
        return Shop_page