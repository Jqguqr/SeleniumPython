from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest


class AssertionsTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(
            executable_path='./web_drivers/chromedriver')
        driver = cls.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")

    def test_search_text_fild_by_xpath(self):
        self.assertTrue(self.is_element_present(
            how=By.XPATH, what="//input[@name='q']"))

    def test_language_option(self):
        self.assertTrue(self.is_element_present(
            how=By.XPATH, what="//select[@id='select-language']"))

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

    # Metodo que nos ayuda a encontrar los elementos
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as variable:
            return False
        return True


if __name__ == "__main__":
    unittest.main(verbosity=2)
