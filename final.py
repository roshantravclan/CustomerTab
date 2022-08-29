import pickle
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(ChromeDriverManager().install())
def autmate():
    driver.maximize_window()
    driver.get("http://s4.mytripkart.in/www.systemthinking.in")
    # wait = WebDriverWait(driver, 30)
    # driver.maximize_window()
    # wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Login']"))).click()
    # time.sleep(2)
    # wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='cellContactNumber']"))).send_keys("8802338434")
    # time.sleep(10)
    # wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Request Otp']"))).click()
    # time.sleep(10)
    # wait.until(
    #     EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']//div//div//div//button[@type='button']"))).click()
    # time.sleep(3)
    # pickle.dump( driver.get_cookies() , open("cookiesfinal.pkl","wb"))
    cookies = pickle.load(open("cookiesfinal.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()

autmate()