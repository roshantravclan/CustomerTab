import time
from csv import DictReader
from random import randint

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://s4.travclan.com/en/my_customers")

driver.maximize_window()
wait = WebDriverWait(driver, 30)


# def get_cookie(file):
#     with open(file, encoding='utf-8-sig') as f:
#         dict_reader = DictReader(f)
#         list_of_dicts = list(dict_reader)
#     return list_of_dicts


# print(get_cookie("b2b.csv"))
# cookies = get_cookie("b2b.csv")
# import ipdb
# ipdb.set_trace()

# for i in cookies:
#     driver.add_cookie(i)
class LocalStorage:
    def __init__(self, driver):
        self.driver = driver

    def set(self, key, value):
        self.driver.execute_script("window.localStorage.setItem(arguments[0], arguments[1]);", key, value)


storage = LocalStorage(driver)
storage.set("user",
            '{"result_code":1001,"status":"success","data":{"member":{"id":27778,"code":"mjdnz","email":"nitinmadeshia@gmail.com","phone":"918860646291","username":"nitinmadeshia_9997596","name":"Nitin Madeshia","family_name":"","company_name":"Adventure Travel","active":true,"deleted":false,"blocked":false,"website":"","created_at":"2021-10-19T17:46:18.985519","updated_at":"2022-04-21T06:21:17.980700","nationality_id":null,"nationality":"<built-in method title of str object at 0x7f8acb7d48b8>","member_hash_id":"caa85af0a845849b141636f0c661b442a4f39415","chat_password":"b)UBiZ#@KnmAV4{UUCbILKHbo0~h;~UZi6CfA4!Hwn;QKaOsjH"},"auth_tokens":{"access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NjE5Mjk1OTQsImlhdCI6MTY2MTMyNDc5NCwic3ViIjoyNzc3OH0.ZvyxN48Hqe_pznGaqMqW9dngTa-8homAd-3szCr3Jzg","refresh_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NjIwMTAxMTgsImlhdCI6MTY1OTQxODExOCwic3ViIjoyNzc3OH0.ev5dMQX7RgFlw8ZpROJyFQ7que2BHgVH6Nr0fuT0P9E"}},"message":"OTP Verified","http_status_code":200}')
driver.get("http://s4.travclan.com/en/my_customers")
# wait.until(EC.presence_of_element_located((By.XPATH ,"//span[@class='MuiButton-label']"))).click()
# element = wait.until(EC.presence_of_element_located((By.XPATH,"(//input[@role='combobox'])[4]")))
# element.click()
# # element.send_keys(Keys.DOWN)
# element.send_keys(Keys.ENTER)
# # wait.until(EC.presence_of_element_located((By.XPATH,"(//div)[177]"))).send_keys("Mr")
# time.sleep(2)
# wait.until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Enter First Name']"))).send_keys("roshan")
# wait.until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Enter Last Name']"))).send_keys("kumar")
# wait.until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Enter Phone Number']"))).send_keys(randint(1000000000, 9999999999))
# wait.until(EC.presence_of_element_located((By.XPATH,"//span[contains(text(), 'Add customer')]"))).click()
elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr[1]/child::td/h6")))
print(len(elements))
for element in elements:
    print(element.get_attribute("outerHTML"))
for element in elements:
    print(element.text)
list = ["Mr Roshan Kumar", "+911083561483", "Customer Created"]

for i in range(len(list)):
    assert list[i] == elements[i].text

