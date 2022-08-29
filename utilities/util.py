class LocalStorage:
    def __init__(self, driver):
        self.driver = driver

    def set(self, key, value):
        self.driver.execute_script("window.localStorage.setItem(arguments[0], arguments[1]);", key, value)
