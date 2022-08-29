import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="class")
def setup(request):
    s = Service("/home/roshan/PycharmProjects/pythonProject2/drivers/chromedriver")
    driver = webdriver.Chrome(service=s)
    driver.get("http://s4.travclan.com/en/my_customers")
    wait = WebDriverWait(driver, 30)
    driver.maximize_window()
    print("Launching Browser")

    request.cls.driver = driver
    request.cls.wait = wait