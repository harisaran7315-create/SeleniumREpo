from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from BrowserUtils import BrowserUtils


class checkOutAndConfirmation(BrowserUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.checkoutButton = (By.CSS_SELECTOR, ".btn.btn.btn-success")
        self.CountrySelection  = (By.CSS_SELECTOR, ".filter-input")
        self.CountryConfirmation  = (By.LINK_TEXT, "India")
        self.checkInBox = (By.XPATH, "//label[@for='checkbox2']")
        self.PurchaseConfirmation = (By.CSS_SELECTOR, ".btn.btn-success")
        self.SuccessMessage = (By.CSS_SELECTOR, ".alert-success")

    def checkout(self):
        self.driver.find_element(*self.checkoutButton).click()

    def Country_Confirmation(self, CountryName):
        self.driver.find_element(*self.CountrySelection).send_keys(CountryName)
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.presence_of_element_located(self.CountryConfirmation)).click()
        self.driver.find_element(*self.checkInBox).click()
        self.driver.find_element(*self.PurchaseConfirmation).click()

    def validate_Purchase(self):
        PurchaseStatus = self.driver.find_element(*self.SuccessMessage).text
        assert "Success" in PurchaseStatus

