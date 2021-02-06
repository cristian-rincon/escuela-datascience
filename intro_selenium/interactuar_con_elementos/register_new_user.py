import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner


class RegisterNewUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='../chromedriver')
        driver = cls.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(30)

    def test_new_user(self):
        driver = self.driver
        driver.find_element_by_xpath(
            '//*[@id="header"]/div/div[2]/div/a/span[2]').click()
        driver.find_element_by_link_text("Log In").click()

        create_account_btn = driver.find_element_by_xpath(
            '//*[@id="login-form"]/div/div[1]/div[2]/a/span/span')
        self.assertTrue(create_account_btn.is_displayed()
                        and create_account_btn.is_enabled())
        create_account_btn.click()
        self.assertEqual('Create New Customer Account', driver.title)

        first_name = driver.find_element_by_id("firstname")
        middle_name = driver.find_element_by_id("middlename")
        last_name = driver.find_element_by_id("lastname")
        email_address = driver.find_element_by_id("email_address")
        password = driver.find_element_by_id("password")
        confirm_password = driver.find_element_by_id("confirmation")
        news_letter_subscription = driver.find_element_by_id("is_subscribed")
        submit_button = driver.find_element_by_xpath(
            '//*[@id="form-validate"]/div[2]/button')

        self.assertTrue(first_name.is_enabled()
                        and middle_name.is_enabled() and last_name.is_enabled())
        self.assertTrue(email_address.is_enabled(
        ) and password.is_enabled() and confirm_password.is_enabled())
        self.assertTrue(news_letter_subscription.is_enabled()
                        and submit_button.is_enabled())

        first_name.send_keys("Test")
        middle_name.send_keys("Test")
        last_name.send_keys("Test")
        email_address.send_keys("test@testing.com")
        password.send_keys("test")
        confirm_password.send_keys("test")
        submit_button.click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(
        output='.',
        report_name=__file__))
