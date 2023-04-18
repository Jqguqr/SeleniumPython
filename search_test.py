from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest
import time


class SearchTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(
            executable_path='./web_drivers/chromedriver')
        driver = cls.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")

    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element(By.XPATH, "//input[@name='q']")
        search_field.clear()
        search_field.send_keys("tee")
        search_field.submit()
        time.sleep(5)

    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element(By.XPATH, "//input[@name='q']")
        search_field.clear()
        search_field.send_keys("salt shaker")
        search_field.submit()
        time.sleep(5)
        # Get Product
        products = driver.find_elements(By.XPATH, "//li[@class='item last']/a")
        self.assertEqual(1, len(products))
        time.sleep(5)

    @classmethod
    def tearDown(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
