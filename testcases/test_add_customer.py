import time

import pytest

from pages.MycustomerPage import MyCustomerPage


@pytest.mark.usefixtures("setUp")
class TestCustomer:
    @pytest.fixture(autouse=True)
    def __set_customer__(self):
        self.add_customer = MyCustomerPage(self.driver, self.wait)

    def test_click_customer(self):
        self.add_customer.customer()

    def test_same_number(self):
        time.sleep(2)
        self.add_customer.customer_with_same_number()
