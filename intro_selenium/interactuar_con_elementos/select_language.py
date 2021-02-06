import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from selenium.webdriver.support.ui import Select


class LanguageOptions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='../chromedriver')
        driver = cls.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(30)

    def test_new_user(self):
        exp_options = ['English', 'French', 'German']
        active_options = []

        select_language = Select(self.driver.find_element_by_id('select-language'))
        self.assertEqual(3, len(select_language.options))

        for option in select_language.options:
            active_options.append(option.text)

        self.assertListEqual(exp_options, active_options)

        self.assertEqual('English', select_language.first_selected_option.text)

        select_language.select_by_visible_text('German')
        self.assertTrue('store=german' in self.driver.current_url)
        select_language = Select(self.driver.find_element_by_id('select-language'))
        select_language.select_by_index(0)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(
        output='.',
        report_name=__file__))
