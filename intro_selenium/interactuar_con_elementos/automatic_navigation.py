import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner


class NavigationTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='../chromedriver')
        driver = cls.driver
        driver.maximize_window()
        driver.get('https://google.com')
        driver.implicitly_wait(15)

    def test_browser_navigation(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('platzi')
        search_field.submit()

        driver.back()
        driver.forward()
        driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(
        output='.',
        report_name=__file__))
