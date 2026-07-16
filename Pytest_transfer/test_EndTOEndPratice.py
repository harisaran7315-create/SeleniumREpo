import json

import pytest

from LoginPage import BrowserAutomation

JsonFilePath = "C:\\Users\HariharanM\\PycharmProjects\\Day_1\\Pytest\Pytest_Folder\\test_EndTOEndPracticeJSON.json"

with open(JsonFilePath) as f:
    JsonFile = json.load(f)
    Test_list = JsonFile["data"]

@pytest.mark.parametrize("Test_list_items", Test_list)
def test_purchase(BrowserInstance, Test_list_items):
    driver = BrowserInstance
    LoginPageLoad = BrowserAutomation(driver)
    print(LoginPageLoad.GetTitle())
    Shopping_page = LoginPageLoad.LoginUp(Test_list_items["username"], Test_list_items["password"])
    print(Shopping_page.GetTitle())
    CheckOut_Confirmation = Shopping_page.add_to_cart(Test_list_items["Mobile"])
    print(CheckOut_Confirmation.GetTitle())
    CheckOut_Confirmation.checkout()
    CheckOut_Confirmation.Country_Confirmation("ind")
    CheckOut_Confirmation.validate_Purchase()




