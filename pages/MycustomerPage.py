import time
from random import randint

import pytest
import self as self
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, wait

from base.base_driver import BaseDriver


class MyCustomerPage(BaseDriver):
    def __init__(self, driver, wait):
        self.number = None
        self.wait = wait
        self.driver = driver
        self.base_object = BaseDriver(driver, wait)

    def customer(self):
        self.base_object.find_element_by_locator(By.XPATH, "//span[@class='MuiButton-label']").click()

        element = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@role='combobox'])[4]")))
        element.click()
        # element.send_keys(Keys.DOWN)
        element.send_keys(Keys.ENTER)
        #        self.wait.until(EC.presence_of_element_located((By.XPATH,"(//div)[177]"))).send_keys("Mr")
        time.sleep(2)
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter First Name']"))).send_keys(
            "dsfkjgs")
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Last Name']"))).send_keys(
            "sdkfgsv")
        self.number = randint(1000000000, 9999999999)
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Phone Number']"))).send_keys(
            self.number)

        elements = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr[1]/child::td/h6")))
        # print(len(elements))
        # for element in elements:
        #     print(element.get_attribute("outerHTML"))
        # for element in elements:
        #     print(element.text)
        # list = ["Mr Roshan Kumar", "+911083561483", "Customer Created"]
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Add customer')]"))).click()
        # for i in range(len(list)):
        #     assert list[i] == elements[i].text

    def customer_with_same_number(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='MuiButton-label']"))).click()
        element = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@role='combobox'])[4]")))
        element.click()
        # element.send_keys(Keys.DOWN)
        element.send_keys(Keys.ENTER)
        #        self.wait.until(EC.presence_of_element_located((By.XPATH,"(//div)[177]"))).send_keys("Mr")
        time.sleep(2)
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter First Name']"))).send_keys(
            "roshan")
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Last Name']"))).send_keys(
            "kumar")
        # print(self.number)
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Phone Number']"))).send_keys(
            "3786540491")

        self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Add customer')]"))).click()

        spanelement = self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(.,'already')]")))
        print(spanelement.text)
