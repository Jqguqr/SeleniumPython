from selenium import webdriver
from pyunitreport import HTMLTestRunner
from selenium.webdriver.common.by import By
import unittest


class HomePageTest(unittest.TestCase):

    # Metodo que se ejecuta antes del casos de prueba
    # Setea todo lo necesario para correr los casos de prueba
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(
            executable_path='./web_drivers/chromedriver')
        driver = cls.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(25)

    # Test Cases
    """
    # Select element by element id
    def test_search_text_fild_by_id(self):
        driver = self.driver
        search_field = driver.find_element(By.ID, "search")

    # Select element by element name
    def test_search_text_fild_by_name(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME, "q")

    # Select element by class name
    def test_search_text_fild_by_class(self):
        driver = self.driver
        search_field = driver.find_element(By.CLASS_NAME, "input-box")

    # Select element by xpath
    def test_search_text_fild_by_xpath(self):
        driver = self.driver
        search_field = driver.find_element(
            By.XPATH, "//div[@class='input-box']")
    """

    # Select element by css selector
    def test_search_text_fild_by_css(self):
        driver = self.driver
        search_field = driver.find_element(
            By.CSS_SELECTOR, ".input-box")

    def test_search_button_enabled(self):
        driver = self.driver
        button = driver.find_element(By.CLASS_NAME, "button")

    def test_count_promo_banner_images(self):
        banner_list = self.driver.find_elements(
            By.XPATH, "//ul[@class='promos']/li/a")
        self.assertEqual(3, len(banner_list))

    # Metodo que se ejecutara al finalizar los casos de prueba
    # Cierra el navegador y libera memoria
    @classmethod
    def tearDown(cls):
        cls.driver.quit()


# Funcion que ejecuta el main que es donde se llaman los casos de prueba
if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(
        output='reports', report_name='search-tests-report'))
