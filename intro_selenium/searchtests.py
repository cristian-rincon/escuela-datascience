import unittest
from unittest.main import main
from pyunitreport import HTMLTestRunner
from selenium import webdriver


class HelloSelenium(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver = cls.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_search_text_field(self):
        self.driver.find_element_by_id("search")

    def test_search_text_field_by_name(self):
        self.driver.find_element_by_name("q")

    def test_search_text_field_by_class_name(self):
        self.driver.find_element_by_class_name("input-text")

    def test_search_button_enabled(self):
        self.driver.find_element_by_class_name("button")

    def test_count_of_promo_banner_images(self):
        banner_list = self.driver.find_element_by_class_name("promos")
        banners = banner_list.find_elements_by_tag_name('img')
        self.assertEqual(3, len(banners))

    def test_vip_promo(self):
        self.driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[4]/a/img')

    def test_shopping_cart(self):
        self.driver.find_element_by_css_selector("div.header-minicart span.icon")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":

    unittest.main(verbosity=2, testRunner=HTMLTestRunner(
        output='.',
        report_name=__file__))

