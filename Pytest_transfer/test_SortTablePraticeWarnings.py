import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.smoke
def test_warnings(BrowserInstance):

    driver = BrowserInstance

    driver.get("https://rahulshettyacademy.com/upload-download-test/")
    # WaitDriver = wait.until(expected_conditions, find)

    driver.find_element(By.XPATH, "//div[text()='Fruit Name']").click()

    BrowserList = driver.find_elements(By.CSS_SELECTOR, "#cell-2-undefined")
    time.sleep(2)
    items_in_list = []

    for items in BrowserList:
        items_in_list.append(items.text)

    items_in_list_copy = items_in_list.copy()

    items_in_list.sort()

    print(items_in_list_copy)
    print(items_in_list)
    assert items_in_list == items_in_list_copy

