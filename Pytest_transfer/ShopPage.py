from selenium.webdriver.common.by import By

from Checkout_and_Confirmatioin import checkOutAndConfirmation
from BrowserUtils import BrowserUtils


class Shop(BrowserUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.ShopLink = (By.CSS_SELECTOR, "a[href*='shop']")
        self.PurchaseList = (By.CSS_SELECTOR, "h4[class='card-title']")
        self.CardButton = (By.CSS_SELECTOR, ".nav-link.btn.btn-primary")
        self.PurchaseCardButton = ()

    def add_to_cart(self, product_name):
        self.driver.find_element(*self.ShopLink).click()
        MobilesPresent = self.driver.find_elements(*self.PurchaseList)
        MobilesFound = []
        for Mobiles in MobilesPresent:
            MobilesFound.append(Mobiles.text)
        MobileOrder = product_name
        assert MobileOrder in MobilesFound
        self.driver.find_element(By.XPATH, "//a[text()='" + MobileOrder + "']/parent::h4/parent::div/parent::div/div/button[@class='btn btn-info']").click()
        self.driver.find_element(*self.CardButton).click()
        CheckOut_Confirmation = checkOutAndConfirmation(self.driver)
        return CheckOut_Confirmation

