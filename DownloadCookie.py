import pickle
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())


def save_cookie(driver):
    with open("cookie", 'wb') as filehandler:
        pickle.dump(driver.get_cookies(), filehandler)


def load_cookie(driver):
    with open("cookie", 'rb') as cookiesfile:
        cookies = pickle.load(cookiesfile)
        for cookie in cookies:
            print(cookie)
            driver.add_cookie(cookie)


driver = webdriver.Chrome(ChromeDriverManager().install())
# url = 'https://www.Youtube.com'
# driver.get(url)
driver.get("http://s4.mytripkart.in/www.systemthinking.in")
wait = WebDriverWait(driver, 30)
driver.maximize_window()
wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Login']"))).click()
time.sleep(2)
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='cellContactNumber']"))).send_keys("8802338434")
time.sleep(10)
wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Request Otp']"))).click()
time.sleep(10)
wait.until(
    EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']//div//div//div//button[@type='button']"))).click()
# first try to login and generate cookies after that you can use cookies to login eveytime
load_cookie(driver)
# Do you task here


pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
save_cookie(driver)
driver.quit()
