import pytest
from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from utilities.util import LocalStorage


@pytest.fixture(scope="class")
def setUp(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://s4.travclan.com/en/my_customers")
    storage = LocalStorage(driver)
    storage.set("user",
            '{"result_code":1001,"status":"success","data":{"member":{"id":27778,"code":"mjdnz","email":"nitinmadeshia@gmail.com","phone":"918860646291","username":"nitinmadeshia_9997596","name":"Nitin Madeshia","family_name":"","company_name":"Adventure Travel","active":true,"deleted":false,"blocked":false,"website":"","created_at":"2021-10-19T17:46:18.985519","updated_at":"2022-04-21T06:21:17.980700","nationality_id":null,"nationality":"<built-in method title of str object at 0x7f8acb7d48b8>","member_hash_id":"caa85af0a845849b141636f0c661b442a4f39415","chat_password":"b)UBiZ#@KnmAV4{UUCbILKHbo0~h;~UZi6CfA4!Hwn;QKaOsjH"},"auth_tokens":{"access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NjE5Mjk1OTQsImlhdCI6MTY2MTMyNDc5NCwic3ViIjoyNzc3OH0.ZvyxN48Hqe_pznGaqMqW9dngTa-8homAd-3szCr3Jzg","refresh_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NjIwMTAxMTgsImlhdCI6MTY1OTQxODExOCwic3ViIjoyNzc3OH0.ev5dMQX7RgFlw8ZpROJyFQ7que2BHgVH6Nr0fuT0P9E"}},"message":"OTP Verified","http_status_code":200}')
    driver.get("http://s4.travclan.com/en/my_customers")
    wait = WebDriverWait(driver, 30)
    driver.maximize_window()
    print("Launching Browser")

    request.cls.driver = driver
    request.cls.wait = wait

