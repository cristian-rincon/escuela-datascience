import unittest
from unittest.main import main
from pyunitreport import HTMLTestRunner
from selenium import webdriver


class HelloSelenium(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='../chromedriver')
        driver = cls.driver
        driver.implicitly_wait(10)

    def test_hello_selenium(self):
        driver = self.driver
        driver.get('https://www.platzi.com')

    def test_wikipedia(self):
        driver = self.driver
        driver.get('https://www.wikipedia.org')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":

    unittest.main(verbosity=2, testRunner=HTMLTestRunner(
        output='reports', report_name='hello_selenium_reports'))
