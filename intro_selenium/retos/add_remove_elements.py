import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner


class AddRemoveElements(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='../chromedriver')
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Add/Remove Elements').click()

    def test_add_remove(self):
        driver = self.driver
        elements_added = int(input('¿How many elements you want to add? \n'))
        elements_removed = int(input('¿How many elements you want to remove? \n'))
        total_elements = elements_added - elements_removed

        add_button = driver.find_element_by_xpath('//*[@id="content"]/div/button')

        for i in range(elements_added):
            add_button.click()

        for i in range(elements_removed):
            try:
                delete_button = driver.find_element_by_xpath('//*[@id="elements"]/button')
                delete_button.click()
            except Exception as e:
                print("You're trying to delete more elements that elements existent")
                print(e)

        if total_elements > 0:
            print(f'There are {total_elements} on screen')
        else:
            print('There are no elements on screen')

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(
        output='.',
        report_name=__file__))
