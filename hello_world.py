from pyunitreport import HTMLTestRunner
from selenium import webdriver
import unittest


class HelloWorld(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path='./web_drivers/chromedriver')
        driver = cls.driver
        driver.implicitly_wait(10)

    def test_hello_world(self):
        driver = self.driver
        driver.get('https://platzi.com')

    def test_visit_wikipedia(self):
        driver = self.driver
        driver.get('https://es.wikipedia.org')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(
        output='reports', report_name='hello-world-report'))
