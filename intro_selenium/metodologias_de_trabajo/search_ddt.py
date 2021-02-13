import csv
import unittest
from ddt import ddt, data, unpack
from pyunitreport import HTMLTestRunner
from selenium import webdriver


def get_data(file_name):
    rows = []
    data_file = open(file_name, 'r')
    reader = csv.reader(data_file)
    next(reader, None)

    for row in reader:
        rows.append(row)
    return rows


@ddt
class SearchDDT(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='../chromedriver')
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(15)

    @data(*get_data('testdata.csv'))
    @unpack
    def test_search_ddt(self, search_value, expected_count):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

        products = driver.find_elements_by_xpath('//h2[@class="product-name"]/a')
        expected_count = int(expected_count)

        if expected_count > 0:
            self.assertEqual(expected_count, len(products))
        else:
            message = driver.find_element_by_class_name('note-msg')
            self.assertEqual('Your search returns no results.', message)
        print(f'{len(products)} products')

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(
        output='.',
        report_name=__file__))
