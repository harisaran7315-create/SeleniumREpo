import pytest
from selenium import webdriver

@pytest.fixture()
def profile_normal():
    print("Hi profile_normal is executed")

@pytest.fixture(scope="class")
def profile():
    print("Execution started")
    name = "hari"
    age = 25
    gender = "male"
    yield name, age, gender
    print("Execution completed")

@pytest.fixture()
def profile2():
    name = "manju"
    age = 24
    gender = "female"
    return [name, age, gender]

@pytest.fixture(params=[("Chrome", "Firefox", "Edge"), ("google", "yahoo", "duck")])
def params_exercise(request):
    return request.param


def pytest_addoption(parser):
    parser.addoption(
        "--SelectedBrowser", action="store", default="edge", help="Browser selection method: chrome or edge"
    )

@pytest.fixture(scope="function")
def BrowserInstance(request):
    SelectedBrowser = request.config.getoption("SelectedBrowser").lower()
    if SelectedBrowser == "chrome":
        Driver = webdriver.Chrome()
    elif SelectedBrowser == "edge":
        Driver = webdriver.Edge()
    Driver.implicitly_wait(5)

    yield Driver
    Driver.close()

    print("Execution completed")



