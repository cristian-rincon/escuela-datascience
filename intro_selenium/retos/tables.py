import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from selenium.common.exceptions import NoSuchElementException


class AddRemoveElements(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='../chromedriver')
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com')
        driver.find_element_by_link_text('Sortable Data Tables').click()

    def test_dynamic_controls(self):
        driver = self.driver
        table_data = []
        try:
            get_rows_table = driver.find_element_by_id('table1').get_property('rows')
            get_head_table = get_rows_table[0].get_property('cells')

            for i in range(1, len(get_rows_table)):
                data = {}
                for j in range(len(get_rows_table)):
                    get_head_cells = get_head_table[j].text
                    get_body_cells = get_rows_table[i].get_property('cells')[j].text

                    data.update({get_head_cells: get_body_cells})
                table_data.append(data)

            print(table_data)

        except NoSuchElementException as ex:
            self.fail(ex.msg)


    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(
        output='.',
        report_name=__file__))
